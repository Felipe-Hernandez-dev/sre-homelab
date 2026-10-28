terraform {
  required_providers {
    proxmox = {
      source  = "bpg/proxmox"
      version = "0.66.0" # Fijamos la versión para evitar que actualizaciones futuras rompan el código (Best Practice SRE)
    }
  }
}

# Configuramos cómo Terraform se conectará a tu servidor físico
provider "proxmox" {
  endpoint = "https://192.168.78.100:8006/"

  # Aceptamos certificados autofirmados (típico en homelabs, en prod usaríamos certificados reales de Let's Encrypt)
  insecure = true

  # Nota: El usuario y la contraseña NO están aquí. 
  # Terraform los buscará inteligentemente en las variables de entorno de tu terminal.
}
# Bloque de "Lectura" (Data Source)
data "proxmox_virtual_environment_nodes" "nodos_fisicos" {}

# Bloque de "Salida" (Output) para mostrar la información en pantalla
output "nombres_de_nodos_disponibles" {
  value       = data.proxmox_virtual_environment_nodes.nodos_fisicos.names
  description = "Lista de nodos físicos en el clúster"
}

# Bloque de "Escritura" (Resource) para crear infraestructura
resource "proxmox_virtual_environment_container" "nodo_prueba" {
  description = "Mi primer nodo gestionado 100% por código"
  node_name   = "pve" # El nombre que nos devolvió el output anterior
  vm_id       = 201   # Usamos un ID nuevo para no pisar tu nodo 200

  unprivileged = true # Best practice de seguridad

  features {
    nesting = true
    fuse    = true
  }
  initialization {
    hostname = "tf-node-01"

    # Inyectamos configuración de Capa 3 al Sistema Operativo
    ip_config {
      ipv4 {
        address = "dhcp"
      }
    }

    user_account {
      keys = [
        "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMM69L5HWM7pNQ5pnE2Txpq03nfEwdr+SrymJL1TMbzc felipe_sre_admin"
      ]
    }
  }

  operating_system {
    # Usamos la plantilla exacta que descargaste con pveam en la Fase 2
    template_file_id = "local:vztmpl/debian-12-standard_12.12-1_amd64.tar.zst"
    type             = "debian"
  }

  disk {
    datastore_id = "sre-storage"
    size         = 4
  }

  network_interface {
    name   = "eth0"
    bridge = "vmbr0"

  }
}
