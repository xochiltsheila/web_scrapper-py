importar  argparse
 registro de importación
registro . basicConfig ( nivel = registro . INFO )

importar  news_page_objects  como  noticias
desde  la  configuración de importación  común

logger  =  registro . getLogger ( __name__ )

def  _news_scraper ( news_site_vid ):
    host  =  config () [ 'news_sites' ] [ news_site_vid ] [ 'url' ]

    registro . info ( f'Empezando raspado para { host } ' )
    página de inicio  =  noticias . Página de inicio ( news_site_vid , host )

    para el  enlace  en la  página de inicio . articulos_vínculos :
        imprimir ( enlace )

if  __name__  ==  "__main__" :
    analizador  =  argparse . ArgumentParser ()

    news_sites_choices  =  list ( config () [ 'news_sites' ]. keys ())
    analizador . add_argument ( 'sitio_noticias' ,
                        help  = 'Los sitios de noticias que desea raspar' ,
                        tipo = str ,
                        opciones = news_sites_choices )

    args  =  analizador . parse_args ()
    _news_scraper ( args . news_site )