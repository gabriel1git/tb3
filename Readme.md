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

Para utilizar as ferramentas do turtlebot3 instale os pacotes abaixo: (será utilizado para gerar mapas)

* sudo apt install ros-humble-turtlebot3-msgs
* sudo apt install ros-humble-turtlebot3

## Preparando ambiente

Após instalar todos os pacotes já estamos preparados para simular a navegação.

Vá para o ambiente de trabalhos ROS(na documentação do ROS, este diretório se chama "ros2_ws") o comando abaixo irá redirecioná-lo:

* cd ~/ros2_ws 

Em seguida compile os pacotes clonados do github para o diretório "src" (ros2_ws/src):

* colcon build

Mapeie os pacotes e ferramentas do ambiente ROS:

* . install/setup.bash

## Para executar a simulação 1

Será necessário utilizar dois terminais e em ambos vá para o ambiente de trabalho do ROS e mapeie os pacotes e ferramentas conforme acima, em seguida execute o comando abaixo para abrir o gazebo com todo ambiente de simulação.

* ros2 launch tb3 tb3_1.launch.py

No segundo terminal execute o comando abaixo para abrir o Rviz2 e iniciar os algoritmos de controle e planejamento de navegação.
* ros2 launch auto_navigation_1.launch.py

## Para executar a simulação 2

Será necessário utilizar dois terminais e em ambos vá para o ambiente de trabalho do ROS e mapeie os pacotes e ferramentas conforme acima, em seguida execute o comando abaixo para abrir o gazebo com todo ambiente de simulação.

* ros2 launch tb3 tb3_2.launch.py

No segundo terminal execute o comando abaixo para abrir o Rviz2 e iniciar os algoritmos de controle e planejamento de navegação.
* ros2 launch auto_navigation_2.launch.py
