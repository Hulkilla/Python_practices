# PAQUETES DISTRIBUIBLES: para poder compartirlos con otros.

# Para ello hay que crear el paquete e instalarlo

#Asi lo podemos utilizar, esté donde esté.

#Lo que vamos a hacer es instalarlo en nuestro programa

from setuptools import setup

setup(
      
      name = "paquetecalculos",
      version = "1.0",
      description = "Paquete de redondeo y potencia",
      author = "Marina Fernández",
      author_mail = "marinafd@gmail.com",
      url = "www.linkedin.com/in/mfd-122567b2",
      packages = ["Creacion_paquetes", "calculos", "calculos.redondeo_potencia"] 
      
      
      )


# Una vez creado deberíamos ir al administrador del sistema y copiar la ruta donde tengamos la carpeta root 

# Es decir, la carpeta donde se encuentra este archivo

# una vez estemos en la carpeta en el administrador del sistema debemos introducir el siguiente comando:
    
    # python setup.py sdist
    
# El admisitrador empieza a funcionar haciendo un montón de ocsas y si todo va bien en nuestra carpeta debería haber creado otras dos

# LAs carpetas se llamarían: dist y paquetecalculos.egg-info

# Si abrimos la carpeta "dist" habrá un archvo .rar connombre "paquetecalculos-1.0.tar.gz" (en este caso, obvio)

# Este es el archivo que podría ser distribuido

# Lo vamos a instalar en nuestro python a partir de la consola de administrador

# En la consola de admiistraor pones la ruta que lleve hasta la carpeta "dist" y escribimos el siguiente comando:
    
    # py -m pip install paquetecalculos-1.0.tar.gz

# Una vez instalado correctamente, se puede utilizar el paquete en nuestros archivos sin problemas, 

# Sin tener en cuenta donde está ubicado el archivo que se ha utilizado para crear el paquete.

# Para desisntalar el paquete, en la consola de administrador la instrucción sería:
    
    # pip3 unistall paquetecalulos
    
    # Nos hace una pregunta de seguridad


