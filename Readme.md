# Simulação de navegação utilizando ROS2 e Gazebo (turtlebot3)

Esta simulação foi desenvolvida no ambiente ROS2 humble, dessa forma caso deseje replicá-la é aconselhavel que utilize a mesma versão.

Este pacote utiliza a biblioteca NAV2 de software do ROS2 (Robot Operating System 2) que oferece um conjunto de ferramentas e algoritmos que permitem a um robô planejar caminhos, evitar obstáculos, e navegar em ambientes mapeados ou não-mapeados.

## pre-requisitos

Será necessário instalar os pacotes "navigation2" e "nav2-bringup" para que possamos utilizar as ferramentas disponibilizadas pelo NAV2.
Execute os comandos abaixo para instala-las:

* sudo apt install ros-humble-navigation2
* sudo apt install ros-humble-nav2-bringup

Caso ainda não tenha o Gazebo instalado execute o comando abaixo para instala-lo:

* sudo apt install ros-humble-gazebo-*

Estes pacotes que serão instalados agora, permite a geração de mapas.

* sudo apt install ros-humble-cartographer
* sudo apt install ros-humble-cartographer-ros

### Preparando ambiente

Após instalar todos os pacotes já estamos preparados para simular a navegação.

Vá para o ambiente de trabalhos ROS(na documentação do ROS, este diretório se chama "ros2_ws") o comenaod abaixo irá redirecioná-lo:

* cd ~/ros2_ws 

Em seguida compile os pacotes clonados do github:

* colcon build

Mapeie os pacotes e ferramentas do ambiente ROS:

* . install/setup.bash

