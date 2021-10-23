importar  yaml

__config  =  Ninguno


def  config ():
     __config global
    si  no es  __config :
        con  open ( 'config.yaml' , mode = 'r' ) como  f :
            __config  =  yaml . carga_segura ( f )
        
    return  __config