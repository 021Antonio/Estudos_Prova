#!/usr/bin/env python3
import rclpy #Faz interfaciamneto do ros python(Uma rota)
from rclpy.node import Node #Classe responsavel pelos nos
from geometry_msgs.msg import Twist #Tipo de dado que o ros recebe referente a movimentação do robo

#Criando a classe do controle da tartaruga
class TurtleController(Node): 
    def __init__(self): #Configurar o sistema plublish/subscriber (talker e listener)
        super().__init__('turtle_controller') 
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10) 
        self.timer_ = self.create_timer(1.0, self.move_turtle) #Cria um timer que a cada 1 segundo chama a função de movimnetação
        self.twist_msg_ = Twist() #Criando uma instancia da classe Twist
        self.aumento_velocidade = 0 #Variavel que vai setar a velocidade

    def move_turtle(self): #Velocidade linear e angular(Função de movimentação)
        self.twist_msg_.linear.x = 0.2 + self.aumento_velocidade * 0.01 #A velocidade linear começa em 0.2 e aumneta em 1
        #a cada volta dada
        self.twist_msg_.angular.z = 0.3 # Seta a movimentação angular 
        self.aumento_velocidade += 1 # A cada volta, x aumenta em 1


        # Um segundo corresponde a uma volta

        
        self.publisher_.publish(self.twist_msg_)


def main(args=None): #Função principal que chama as outras funçoes
    rclpy.init()
    turtle_controller = TurtleController() #Cria uma instancia da classe TurtleController
    rclpy.spin(turtle_controller) 
    turtle_controller.destroy_node() 
    rclpy.shutdown() #Desliga o sistema


if __name__ == '__main__': #Chama a função main
    main()
