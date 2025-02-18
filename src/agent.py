import pandas as pd
import openai
import requests
import json
from decouple import config

API_KEY = config("API_KEY")
API_URL = config("API_URL")
FB_ACCESS_TOKEN = config("FB_ACCESS_TOKEN")
FB_VERIFY_TOKEN = config("FB_VERIFY_TOKEN")
WP_URL = config("WP_URL")


def generar_comparacion_ia(texto_comparacion):
    print(texto_comparacion)
    headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
    }

    productos = [
    {
        "Código": "TPM430003-3015",
        "NOMBRE DEL PRODUCTO": "HORSE GREEN                                                       ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003015",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Amaderada Chipre para Hombres\nLas Notas de Salida son bayas de enebro, albahaca, abrótano, alcaravea, cilantro y bergamota;\nlas Notas de Corazón son agujas de pino, cuero, manzanilla, pimienta, clavel, geranio, jazmín y rosa;\nlas Notas de Fondo son tabaco, musgo de roble, pachulí, cedro, vetiver, almizcle y ámba",
        "UNIDAD DE MEDIDA": "90",
        "PESO DEL PRODUCTO": "250",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: POLO de Ralph Lauren"
    },
    {
        "Código": "TPM430004-3022",
        "NOMBRE DEL PRODUCTO": "HORSE BLUE                                                            ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003022",
        "DESCRIPCION DEL PRODUCTO": "Es una fragancia de la familia olfativa Aromática Fougère para Hombres. \nLas Notas de Salida son pepino, melón y mandarina; las Notas de Corazón son albahaca, salvia y geranio; las Notas de Fondo son gamuza, notas amaderadas y almizcle.",
        "UNIDAD DE MEDIDA": "90",
        "PESO DEL PRODUCTO": "250",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: POLO de Ralph Lauren"
    },
    {
        "Código": "TPM-430005-0809",
        "NOMBRE DEL PRODUCTO": "HORSE BLACK                                                          ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543000809",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Amaderada Aromática para Hombres. \nSALIDA Mango, Artemisia (ajenjo), Limón italiano, Albahaca\nCORAZON Verbena de limón, Salvia , Hedione ,Violeta negra\nFONDO Pachulí , Madera de sándalo ,Vetiver ,cedro.",
        "UNIDAD DE MEDIDA": "80",
        "PESO DEL PRODUCTO": "250",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA  Polo Black de Ralph Lauren"
    },
    {
        "Código": "TP-430006-0847",
        "NOMBRE DEL PRODUCTO": "HORSE RED                                                             ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543000847",
        "DESCRIPCION DEL PRODUCTO": "Es una fragancia de la familia olfativa Amaderada Especiada para Hombres.\nLas Notas de Salida son arándano, toronja (pomelo) y limón italiano (lima italiana); las Notas de Corazón son azafrán y salvia; las Notas de Fondo son ámbar, café y notas amaderadas.",
        "UNIDAD DE MEDIDA": "90",
        "PESO DEL PRODUCTO": "270",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: POLO RED de Ralph Lauren"
    },
    {
        "Código": "TPM-430007-3510",
        "NOMBRE DEL PRODUCTO": "HORSE RED INTENSE                                              ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003510",
        "DESCRIPCION DEL PRODUCTO": "Es una fragancia de la familia olfativa Amaderada Especiada para Hombres.\nLas Notas de Salida son arándano, toronja sanguina, limón (lima ácida) y azafrán; las Notas de Corazón son café, jengibre, lavanda y salvia; las Notas de Fondo son ámbar, cuero y cedro rojo japonés. ",
        "UNIDAD DE MEDIDA": "80",
        "PESO DEL PRODUCTO": "270",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: POLO RED INTENS de Ralph Lauren"
    },
    {
        "Código": "TPM-430008-3691 ",
        "NOMBRE DEL PRODUCTO": "HORSE SUPREME OUD                                           ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792516003691",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Ámbar Amaderada para Hombres.\nLas Notas de Salida son canela y pimienta rosa;\nla Nota de Corazón es madera de oud;\nlas Notas de Fondo son madera de gaiac y vetiver.",
        "UNIDAD DE MEDIDA": "80",
        "PESO DEL PRODUCTO": "270",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA  Polo Supreme Oud de Ralph Lauren"
    },
    {
        "Código": "TPM-430009-1622",
        "NOMBRE DEL PRODUCTO": "ORIXA POUR HOMME                                               ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543001622",
        "DESCRIPCION DEL PRODUCTO": "Es una fragancia de la familia olfativa Amaderada Acuática para Hombres.\nLas Notas de Salida son yuzu, limón (lima ácida), bergamota, cedrón (hierba luisa, verbena de olor), mandarina, ciprés, calone, cilantro, estragón y salvia; las Notas de Corazón son flor de loto azul, nuez moscada, lirio de los valles (muguete), azafrán, canela de Ceylan, geranio bourbon y reseda (miñoneta); las Notas de Fondo son vetiver de Tahití, almizcle, cedro, sándalo, tabaco y ámbar.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "290",
        "ATRIBUTOS DEL PRODUCTO": "Inspirado en L'Eau d'Issey pour Homme de Issey Miyake"
    },
    {
        "Código": "TPM-430010-0823",
        "NOMBRE DEL PRODUCTO": "D`ORGEVAL CODE MEN                                            ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543000823",
        "DESCRIPCION DEL PRODUCTO": "FAMILIA OLFATIVA : ámbar especiada\nSALIDA : Limón , bergamota\nCORAZON : anís estrellado , flor de olivo , madera de gaiac\nFONDO : Cuero , haba tonka ,tabaco",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA : Armani Code Ultimate de Giorgio Armani"
    },
    {
        "Código": "TPM-430011-2896",
        "NOMBRE DEL PRODUCTO": "YD ONE  - UNISEX                                                   ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543002896",
        "DESCRIPCION DEL PRODUCTO": "Las Notas de Salida son limón (lima ácida), notas verdes, bergamota, piña, mandarina, cardamomo y papaya; las Notas de Corazón son lirio de los valles (muguete), jazmín, violeta, nuez moscada, rosa, raíz de lirio y fresia; las Notas de Fondo son acordes verdes, almizcle, cedro, sándalo, musgo de roble, té verde y ámbar.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "320",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: ONE UNISEX BY CALVIN KLEIN"
    },
    {
        "Código": "TPM-430012-2827",
        "NOMBRE DEL PRODUCTO": "GH MEN                                                                   ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543002827",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Ámbar Especiada para Hombres.\nLas Notas de Salida son hierba, bergamota y toronja (pomelo);\nlas Notas de Corazón son notas amaderadas, nuez moscada, violeta, azafrán y jazmín;\nlas Notas de Fondo son azúcar, cuero, vainilla, gamuza, ámbar, madera de cachemira, sándalo, musgo de roble y vetiver.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA CH Men de Carolina Herrera "
    },
    {
        "Código": "TPM-430013-3848",
        "NOMBRE DEL PRODUCTO": "GH CLASSIC                                                             ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003848",
        "DESCRIPCION DEL PRODUCTO": " es una fragancia de la familia olfativa Almizcle Amaderado Floral para Hombres\nLas Notas de Salida son limón (lima ácida), lavanda, romero y neroli; las Notas de Corazón son clavos de olor, geranio y trébol blanco; las Notas de Fondo son tabaco, sándalo y ámbar gris.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA HERRERA for Men de CAROLINA HERRERA"
    },
    {
        "Código": "TPM-430014-3077",
        "NOMBRE DEL PRODUCTO": "JENKO                                                                     ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003077",
        "DESCRIPCION DEL PRODUCTO": " es una fragancia de la familia olfativa Amaderada Acuática para Hombres.\nLas Notas de Salida son menta, cítricos y cardamomo;\nlas Notas de Corazón son notas marinas, salvia y especias;\nlas Notas de Fondo son sándalo, vetiver, cedro y vainilla.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA  Kenzo Homme Eau de Parfum de Kenzo"
    },
    {
        "Código": "TPM-430016-3275",
        "NOMBRE DEL PRODUCTO": "HYDO RED                                                                ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003275",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Floral Frutal Gourmand para Mujeres.\nLas Notas de Salida son grosellas negras y pera\nlas Notas de Corazón son iris, jazmín y flor de azahar del naranjo;\nlas Notas de Fondo son praliné, vainilla, pachulí y haba tonka.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA  Hugo Red de Hugo Boss"
    },
    {
        "Código": "TPM-430017-3268",
        "NOMBRE DEL PRODUCTO": "HYDO JUST DIFFERENT                                             ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003268",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Aromática para Hombres. \nLas Notas de Salida son menta y manzana Granny Smith;\nlas Notas de Corazón son albahaca, fresia y cilantro;\nlas Notas de Fondo son cachemira, pachulí, incienso de olíbano (franquincienso) y ládano|",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA Hugo Just Different de Hugo Boss"
    },
    {
        "Código": "TPM-430018-2988",
        "NOMBRE DEL PRODUCTO": "HYDO                                                                       ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543002988",
        "DESCRIPCION DEL PRODUCTO": " es una fragancia de la familia olfativa Aromática Verde para Hombres. \nLas Notas de Salida son manzana verde, menta, lavanda, toronja (pomelo) y albahaca;\nlas Notas de Corazón son salvia, geranio, clavel y jazmín; las Notas de Fondo son abeto, cedro y pachulí.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "360",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA Hugo de Hugo Boss"
    },
    {
        "Código": "TPM-430020-3503",
        "NOMBRE DEL PRODUCTO": "CELSIUS                                                                   ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003503",
        "DESCRIPCION DEL PRODUCTO": " Las Notas de Salida son flor del moscadero, lavanda, cedro, manzanilla, mandarina, flor del espino, bergamota y limón (lima ácida);\nlas Notas de Corazón son hojas de violeta, nuez moscada, cedro, sándalo, clavel, madreselva, jazmín y lirio de los valles (muguete);\nlas Notas de Fondo son cuero, vetiver, almizcle, ámbar, pachulí y haba tonka.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "340",
        "ATRIBUTOS DEL PRODUCTO": "EEQUIVALENCIA : FAHRENHEIT DIOR"
    },
    {
        "Código": "TPM-430021-3527",
        "NOMBRE DEL PRODUCTO": "ACQUA DI YDO                                                         ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003527",
        "DESCRIPCION DEL PRODUCTO": " Las Notas de Salida son lima (limón verde), limón (lima ácida), bergamota, jazmín, naranja, mandarina y neroli; las Notas de Corazón son notas marinas, jazmín, calone, durazno romero, fresia, jacinto, cilantro, violeta, nuez moscada, rosa y reseda las Notas de Fondo son almizcle blanco, cedro, musgo de roble, pachulí",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "330",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA ACQUA DI GIO para hombres by GIORGIO ARMANI"
    },
    {
        "Código": "TPM-430024-3763",
        "NOMBRE DEL PRODUCTO": "GH PRIVE MEN                                                          ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003763",
        "DESCRIPCION DEL PRODUCTO": " es una fragancia de la familia olfativa Cuero para Hombres\nLas Notas de Salida son whisky y pomelo ; las Notas de Corazón son cardamomo, lavanda, salvia y tomillo rojo; las Notas de Fondo son cuero, haba tonka, notas amaderadas y benjuí.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "320",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA CH PRIVÉ for Men de CAROLINA HERRERA"
    },
    {
        "Código": "TPM-430026-2995",
        "NOMBRE DEL PRODUCTO": "BLACK YD                                                                 ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543002995",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Ámbar Amaderada para Hombres.\nLas Notas de Salida son limón (lima ácida) y salvia;\nlas Notas de Corazón son praliné, canela, bálsamo de Tolú y cardamomo negro;\nlas Notas de Fondo son palo de rosa de Brasil, pachulí y ámbar negro.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA Black XS for Men de Paco Rabanne "
    },
    {
        "Código": "TPM-430027-3862",
        "NOMBRE DEL PRODUCTO": "BLACK YD L`APHRODISIAQUE                                                           ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003862",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Cuero para Hombres\n. Las Notas de Salida son canela y azafrán;\nlas Notas de Corazón son miel, flor de azahar del naranjo y ciprés;\nlas Notas de Fondo son praliné, cuero y almendra.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "340",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA Black XS L'Aphrodisiaque for Men de Paco Rabanne"
    },
    {
        "Código": "TPM-430028-0748",
        "NOMBRE DEL PRODUCTO": " BLACK YD L'ELIXIR                                                  ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543000748",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Amaderada Aromática para Hombres.\nLas Notas de Salida son limón de Amalfi (lima de Amalfi) y lavanda;\nlas Notas de Corazón son cipriol (nagarmota) y notas marinas;\nlas Notas de Fondo son ámbar y pachulí.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "340",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA Black XS L'EXCES for Men de Paco Rabanne "
    },
    {
        "Código": "TPM-430030-3114",
        "NOMBRE DEL PRODUCTO": "YD12 MEN (Especial)                                                  ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003114",
        "DESCRIPCION DEL PRODUCTO": "Las Notas de Salida son notas verdes, toronja (pomelo), especias, bergamota, lavanda y petit grain;\nlas Notas de Corazón son jengibre, violeta, gardenia y salvia;\nlas Notas de Fondo son almizcle, sándalo, incienso, vetiver, madera de gaiac y ládano.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "340",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA : 212 Men de Carolina Herrera "
    },
    {
        "Código": "TPM-430031-3121",
        "NOMBRE DEL PRODUCTO": "YD12 SEXY MEN (Especial)                                        ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 40,000 ",
        "CODIGO DE BARRA ": "7792543003121",
        "DESCRIPCION DEL PRODUCTO": "Es una fragancia de la familia olfativa Ámbar Fougère para Hombres. \nLas Notas de Salida son mandarina, bergamota y notas verdes; las Notas de Corazón son pimienta, flores y cardamomo; las Notas de Fondo son vainilla, madera de gaiac, sándalo, ámbar y almizcle.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "340",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: 212 SEXY MEN BY CAROLINA HERRERA"
    },
    {
        "Código": "TPM-430032-3664",
        "NOMBRE DEL PRODUCTO": "YD12 VIP NIGHT CLUB MEN                                       ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003664",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Amaderada Especiada para Hombres. \nNotas de Salida son lima (limón verde), notas acuosas y caviar;\nlas Notas de Corazón son nuez moscada, notas amaderadas y pimienta;\nlas Notas de Fondo son chocolate y notas amaderadas.",
        "UNIDAD DE MEDIDA": "110",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA :212 VIP Men Club Edition de Carolina Herrera "
    },
    {
        "Código": "TPM-430033-3794",
        "NOMBRE DEL PRODUCTO": "YD12 VIP MEN (CRISTAL)                                           ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003794",
        "DESCRIPCION DEL PRODUCTO": "Nota Olfativas Principales Las Notas de Salida son de Maracuyá, Lima Verde, Pimienta y Jengibre; las Notas de Corazón so Vodka, Ginebra, Menta y Especias; las Notas de Fondo son Ambar, Cuero y Notas Amaderadas.",
        "UNIDAD DE MEDIDA": "110",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: 212 VIP MEN CRISTAL BY CAROLINA HERRERA"
    },
    {
        "Código": "TPM-430034-3350",
        "NOMBRE DEL PRODUCTO": "VICTORIOUS (Especial)                                             ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003350",
        "DESCRIPCION DEL PRODUCTO": "Las Notas de Salida son notas marinas, toronja (pomelo) y mandarina; las Notas de Corazón son hoja de laurel y jazmín; las Notas de Fondo son ámbar gris, madera de gaiac, musgo de roble y pachulí.",
        "UNIDAD DE MEDIDA": "110",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: INVICTUS MEN BY PACO RABANNE"
    },
    {
        "Código": "TPM-430035-3558",
        "NOMBRE DEL PRODUCTO": "VICTORIOUS GRAND (Especial)                                                          ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003558",
        "DESCRIPCION DEL PRODUCTO": " Es una fragancia de la familia olfativa Ámbar para Hombres.\nLas Notas de Salida son pimienta rosa y limón (lima ácida); las Notas de Corazón son lavanda y incienso de olíbano (franquincienso); las Notas de Fondo son vainilla, haba tonka y ámbar.",
        "UNIDAD DE MEDIDA": "110",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: INVICTUS GOLD BY PACO RABANNE"
    },
    {
        "Código": "TPM-430036-3930",
        "NOMBRE DEL PRODUCTO": "VICTIRIOUS AQUA (Especial)                                    ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003930",
        "DESCRIPCION DEL PRODUCTO": " es una fragancia de la familia olfativa Amaderada Acuática para Hombres. \nLas Notas de Salida son yuzu, toronja (pomelo) y pimienta rosa;\nlas Notas de Corazón son agua de mar y hojas de violeta;\nlas Notas de Fondo son ámbar gris, Amberwood y madera de gaiac.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA Invictus Aqua de Paco Rabanne"
    },
    {
        "Código": "TP-430037-4456",
        "NOMBRE DEL PRODUCTO": "VICTORIOUS INTENSE                                              ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004456",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Amaderada Acuática para Hombres.\nLas Notas de Salida son notas marinas, toronja (pomelo) y mandarina\nlas Notas de Corazón son hoja de laurel y jazmín;\nlas Notas de Fondo son ámbar gris, madera de gaiac, musgo de roble y pachulí.",
        "UNIDAD DE MEDIDA": "110",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA Invictus Intense de Paco Rabanne"
    },
    {
        "Código": "TPM-430038-3039",
        "NOMBRE DEL PRODUCTO": "YD ANGE (Especial)                                                   ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003039",
        "DESCRIPCION DEL PRODUCTO": "Es una fragancia de la familia olfativa Ámbar Amaderada para Hombres. \nLas Notas de Salida son lavanda, menta, notas afrutadas y especiadas, cilantro, notas verdes y bergamota; las Notas de Corazón son caramelo, pachulí, miel, leche, cedro, jazmín y lirio de los valles (muguete); las Notas de Fondo son café, pachulí, vainilla, haba tonka, benjuí, ámbar, sándalo y almizcle.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "340",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: angel thierry mugler hombre"
    },
    {
        "Código": "TPM-430039-4432",
        "NOMBRE DEL PRODUCTO": "G. MILLIONAIRE GOLD                                                                         ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004432",
        "DESCRIPCION DEL PRODUCTO": "Es una fragancia de la familia olfativa Amaderada Especiada para Hombres.\nLas Notas de Salida son mandarina roja, toronja (pomelo) y menta; las Notas de Corazón son canela, notas especiadas y rosa; las Notas de Fondo son ámbar, cuero, notas amaderadas y pachulí hindú",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: ONE MILLION BY PACO RABANNE"
    },
    {
        "Código": "TPM-430040-3954",
        "NOMBRE DEL PRODUCTO": "G. MILLIONAIRE PRIVE                                             ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003954",
        "DESCRIPCION DEL PRODUCTO": " oriental amaderado para hombres.\nSALIDA canela mandarina\nCORAZON tabaco mirra\nFONDO haba tonka pachuli.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA ONE MILLION PRIVÉ for Men de Paco Rabanne"
    },
    {
        "Código": "TPM-430043-3916",
        "NOMBRE DEL PRODUCTO": "PIPE DREAM                                                              ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003916",
        "DESCRIPCION DEL PRODUCTO": "FAMILIA OLFATIVA : amaderada\nSALIDA pimienta rosa,canela, bergamota\nCORAZON tabaco dulce ,cardamomo.\nFONDO ambroxan , sándalo, madera de gaiac , cedro , vetiver, pachuli, vainilla,haba tonka",
        "UNIDAD DE MEDIDA": "35",
        "PESO DEL PRODUCTO": "70",
        "ATRIBUTOS DEL PRODUCTO": "Es una creacion Original de DEORGEVAL"
    },
    {
        "Código": "TPM-430044-39223",
        "NOMBRE DEL PRODUCTO": "PIPE DREAM OUD                                                      ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543003923",
        "DESCRIPCION DEL PRODUCTO": "FAMILIA OLFATIVA : Amaderada \nSALIDA :canela, oud, bergamota, pimienta suave\nCORAZON :cardamomo , vainilla , oud , haba tonka, \nFONDO : almizcle, madera de Agar , ambroxan , vetiver ",
        "UNIDAD DE MEDIDA": "35",
        "PESO DEL PRODUCTO": "70",
        "ATRIBUTOS DEL PRODUCTO": "Es una creacion Original de DEORGEVAL"
    },
    {
        "Código": "TPM-430045-4128",
        "NOMBRE DEL PRODUCTO": "COSTA AZUL UNISEX                                                ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004128",
        "DESCRIPCION DEL PRODUCTO": "Es una fragancia de la familia olfativa Amaderada Aromática para Hombres y Mujeres.\nLas Notas de Salida son bayas de enebro, limón (lima ácida) y mirto; las Notas de Corazón son ciprés y agujas de pino; las Notas de Fondo son resina almáciga del lentisco, ámbar y ládano.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "290",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: Tom Ford Costa Azzurra Eau de Parfum"
    },
    {
        "Código": "TPM-430046-4111",
        "NOMBRE DEL PRODUCTO": "NEROLI PORTOBELLO UNISEX                                                           ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004111",
        "DESCRIPCION DEL PRODUCTO": " es una fragancia de la familia olfativa Cítrica Aromática para Hombres y Mujeres\nLas Notas de Salida son bergamota, mandarina, limón (lima ácida), naranja amarga, lavanda, romero y mirto; las Notas de Corazón son flor del naranjo africano, neroli, jazmín y azahar de la China; las Notas de Fondo son ámbar, angélica y almizcle ambreta.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "290",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA Neroli Portofino de Tom Ford ( UNISEX)"
    },
    {
        "Código": "TPM-430047-4043",
        "NOMBRE DEL PRODUCTO": "OUD GOOD                                                               ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004043",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Oriental Amaderada para Hombres y Mujeres\n La fragrancia contiene madera de oud, palo de rosa de Brasil\n, cardamomo, pimienta de Sichuan, sándalo,\nvetiver, haba tonka, vainilla y ámbar..",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "290",
        "ATRIBUTOS DEL PRODUCTO": ""
    },
    {
        "Código": "EQUIVALENCIA Oud Wood de Tom Ford \"",
        "NOMBRE DEL PRODUCTO": "",
        " PRECIO DE VENTA EN PESOS ARGENT": "",
        "CODIGO DE BARRA ": "",
        "DESCRIPCION DEL PRODUCTO": "",
        "UNIDAD DE MEDIDA": "",
        "PESO DEL PRODUCTO": "",
        "ATRIBUTOS DEL PRODUCTO": ""
    },
    {
        "Código": "TPM-430048-4166",
        "NOMBRE DEL PRODUCTO": "SHAPIRO                                                                   ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004166",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Ámbar Amaderada para Hombres y Mujeres.\nLas Notas de Salida son pimienta rosa, almizcle ambreta y bergamota;\nlas Notas de Corazón son gamuza, abedul y jazmín;\nlas Notas de Fondo son abedul, madera de oud y vainilla.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "290",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA OUD SHAPIR by ATELIER ( UNISEX)"
    },
    {
        "Código": "TPM-430049-4142",
        "NOMBRE DEL PRODUCTO": "ORCHIDEE NOIR                                                        ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004142",
        "DESCRIPCION DEL PRODUCTO": "Las Notas de Salida son trufa, gardenia, grosellas negras, ylang-ylang, jazmín, bergamota, mandarina y limón de Amalfi (lima de Amalfi);\nlas Notas de Corazón son orquídea, especias, gardenia, notas afrutadas, ylang-ylang, jazmín y flor de loto;\nlas Notas de Fondo son chocolate mexicano, pachulí, vainilla, incienso, ámbar, sándalo, vetiver y almizcle blanco. .",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "280",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA Black Orchid de Tom Ford ( UNISEX ) "
    },
    {
        "Código": "TPM-430050-4180",
        "NOMBRE DEL PRODUCTO": "YD12 VIP BLACK                                                       ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004180",
        "DESCRIPCION DEL PRODUCTO": "  es una fragancia de la familia olfativa Aromática Fougère para Hombres\n Las Notas de Salida son absenta, anís e hinojo;\nla Nota de Corazón es lavanda;\nlas Notas de Fondo son vaina de vainilla negra y almizcle.",
        "UNIDAD DE MEDIDA": "110",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA : 212 VIP Black de Carolina Herrera\n"
    },
    {
        "Código": "TPM-430051-4197",
        "NOMBRE DEL PRODUCTO": "PURE YD                                                                    ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004197",
        "DESCRIPCION DEL PRODUCTO": " es una fragancia de la familia olfativa Aromática Especiada para Hombres. \nLas Notas de Salida son jengibre, tomillo, toronja (pomelo), bergamota y acordes verdes;\nlas Notas de Corazón son vainilla, Licor, canela, cuero y manzana;\nlas Notas de Fondo son mirra, azúcar, cedro, notas amaderadas, cachemira y pachulí.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "340",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA  Pure XS de Paco Rabanne"
    },
    {
        "Código": "TPM-430052-4203",
        "NOMBRE DEL PRODUCTO": "G. MILLIONAIRE MONEY                                           ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004203",
        "DESCRIPCION DEL PRODUCTO": "Es una fragancia de la familia olfativa Amaderada Especiada para Hombres.\nLas Notas de Salida son azafrán, pimienta negra, mandarina roja y cardamomo; las Notas de Corazón son canela, rosa y neroli; las Notas de Fondo son cuero, sándalo, pachulí y raíz de lirio.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "340",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: ONE MILLION INTENSE BY PACO RABANNE"
    },
    {
        "Código": "TPM-430054-4487",
        "NOMBRE DEL PRODUCTO": "G. MILLONAIRE LUCKIEST                                        ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004487",
        "DESCRIPCION DEL PRODUCTO": "Las Notas de Salida son ciruela, notas ozónicas, toronja (pomelo) y bergamota; las Notas de Corazón son avellana, miel, cedro, madera de cachemira, jazmín y flor de azahar del naranjo; las Notas de Fondo son Amberwood, pachulí, musgo de roble y vetiver",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "340",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: ONE MILLION LUCKY BY PACO RABANNE"
    },
    {
        "Código": "TPM-430055-4470",
        "NOMBRE DEL PRODUCTO": "PURE YD NIGHT                                                        ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004470",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Ámbar Especiada para Hombres. \nLas Notas de Salida son ginseng y jengibre;\nlas Notas de Corazón son cacao, vainilla y canela;\nlas Notas de Fondo son caramelo y mirra.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "340",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA  Pure XS Night de Paco Rabanne"
    },
    {
        "Código": "TPM-430056-4500",
        "NOMBRE DEL PRODUCTO": "XAVIER ROUGE                                                         ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004500",
        "DESCRIPCION DEL PRODUCTO": " es una fragancia de la familia olfativa Ámbar Fougère para Hombres.\nLas Notas de Salida son cactus, naranja china y estragón;\nlas Notas de Corazón son pimiento morrón, geranio africano y cedro;\nlas Notas de Fondo son sándalo, cedro y almizcle blanco.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "340",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA Xeryus Rouge de Givenchy"
    },
    {
        "Código": "TPM-430057-4814",
        "NOMBRE DEL PRODUCTO": "WILDEST                                                                   ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004814",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Aromática Fougère para Hombres. \nLas Notas de Salida son bergamota de Calabria y pimienta;\nlas Notas de Corazón son pimienta de Sichuan, lavanda, pimienta rosa, vetiver, pachulí, geranio y elemí;\nlas Notas de Fondo son ambroxan, cedro y ládano.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "340",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA  Sauvage de Dior "
    },
    {
        "Código": "TPM-430058-4821",
        "NOMBRE DEL PRODUCTO": "GOOD BOY                                                                ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004821",
        "DESCRIPCION DEL PRODUCTO": "Es una fragancia de la familia olfativa Ámbar Especiada para Hombres. Esta fragrancia es nueva. \nLas Notas de Salida son pimienta blanca, pimienta negra y bergamota; las Notas de Corazón son salvia y cedro; las Notas de Fondo son haba tonka, cacao y Amberwood.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: BAD BOY POR CAROLINA HERRERA"
    },
    {
        "Código": "TPM-430059-4890",
        "NOMBRE DEL PRODUCTO": "YD FOR ALL UNISEX                                                 ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004890",
        "DESCRIPCION DEL PRODUCTO": "Notas Olfativas Principales La salida es de aceite de Naranja y Genjibre. Con notas Acuosas y Te. Sobre un Fondo de Almizcle, Cedro, Ambar y Patchouli.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "350",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: Everyone by Calvin Klein"
    },
    {
        "Código": "TPM-430060-4937",
        "NOMBRE DEL PRODUCTO": "VICTORIOUS ONYX                                                   ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 46,000 ",
        "CODIGO DE BARRA ": "7792543004937",
        "DESCRIPCION DEL PRODUCTO": "Fragancia masculina.\nNotas Olfativas: notas marinas, pomelo, jazmín, Pachuli, Madera",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "340",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA:Invictus ONYX By Paco Rabanne"
    },
    {
        "Código": "TPM-430061-4920",
        "NOMBRE DEL PRODUCTO": "GOOD BOY PARFUM                                                 ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543004920",
        "DESCRIPCION DEL PRODUCTO": "Fragancia masculina.\nNotas olfativas: Pimienta negra, cuero y pomelo.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "330",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: Bad Body por Carolina Herrera"
    },
    {
        "Código": "TPM-430063-4951",
        "NOMBRE DEL PRODUCTO": "YD 12 SKATE - PATINETA                                          ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 50,000 ",
        "CODIGO DE BARRA ": "7792543004951",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Aromática Frutal para Hombres.\nLas Notas de Salida son pera, marihuana (cannabis) y jengibre; las Notas de Corazón son geranio y salvia; las Notas de Fondo son almizcle y cuero.",
        "UNIDAD DE MEDIDA": "85",
        "PESO DEL PRODUCTO": "290",
        "ATRIBUTOS DEL PRODUCTO": "INSPIRADO EN 212 Heroes de Carolina Herrera"
    },
    {
        "Código": "TPM-430064-5088",
        "NOMBRE DEL PRODUCTO": "OPTIMUS YD                                                              ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 50,000 ",
        "CODIGO DE BARRA ": "7792543005088",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Amaderada Aromática para Hombres. \nLas Notas de Salida son lavanda, Entusiasmo de limón y limón de Amalfi (lima de Amalfi)\nlas Notas de Corazón son lavanda, Notas terrosas, manzana, Humo y pachulí;\nlas Notas de Fondo son vainilla, lavanda y vetiver",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "250",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA Phantom de Paco Rabanne "
    },
    {
        "Código": "TPM-430065-5095",
        "NOMBRE DEL PRODUCTO": "OPTIMUS LEGION                                                      ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 49,020 ",
        "CODIGO DE BARRA ": "7792543005095",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa para Hombres. Esta fragrancia es nueva.\nLas Notas de Salida son Entusiasmo de limón, lavanda y limón (lima ácida);\nlas Notas de Corazón son pachulí, lavanda, Humo, manzana y Notas terrosas;\nlas Notas de Fondo son lavanda, vetiver y vainilla.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "330",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: POLO de Ralph LaurenEQUIVALENCIA  Phantom Legion de Paco Rabanne"
    },
    {
        "Código": "TPM-430066-5132",
        "NOMBRE DEL PRODUCTO": "ADVENTURE                                                              ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 50,000 ",
        "CODIGO DE BARRA ": "7792543005132",
        "DESCRIPCION DEL PRODUCTO": " es una fragancia de la familia olfativa Chipre Frutal para Hombres.\nLas Notas de Salida son bergamota, grosellas negras, manzana, limón (lima ácida) y pimienta rosa;\nlas Notas de Corazón son piña, pachulí y jazmín de Marruecos;\nlas Notas de Fondo son abedul, almizcle, musgo de roble, ambroxan y cedro",
        "UNIDAD DE MEDIDA": "120",
        "PESO DEL PRODUCTO": "320",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA  Aventus de Creed"
    },
    {
        "Código": "TPM-430067-5156",
        "NOMBRE DEL PRODUCTO": "GOOD BOY COBALT                                                  ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543005156",
        "DESCRIPCION DEL PRODUCTO": " Las Notas Olfativas son: Pimienta rosa, lavanda, geranio, ciruela negra y vetiver ",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "300",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA:Bad Boy Cobalt By Carolina Herrera"
    },
    {
        "Código": "TPM-430068-5170",
        "NOMBRE DEL PRODUCTO": "PARISMANIA Pour Homme                                        ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543005170",
        "DESCRIPCION DEL PRODUCTO": "Las Notas Olfativas son: Caramelo, vetiver, amaderado y salvia esclarea",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "330",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: SCANDAL BY JEAN PAUL GAULTIER"
    },
    {
        "Código": "TPM-430069-5149",
        "NOMBRE DEL PRODUCTO": "WILDEST ELIXIR                                                        ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543005149",
        "DESCRIPCION DEL PRODUCTO": "es una fragancia de la familia olfativa Aromática para Hombres. \nLas Notas de Salida son nuez moscada, canela, cardamomo y toronja (pomelo);\nla Nota de Corazón es lavanda;\nlas Notas de Fondo son regaliz, sándalo, ámbar, pachulí y vetiver",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "320",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA Sauvage Elixir de Dior"
    },
    {
        "Código": "TPM-430070-5194",
        "NOMBRE DEL PRODUCTO": "FCKNG FASHION - UNISEX ",
        " PRECIO DE VENTA EN PESOS ARGENT": " $ 45,000 ",
        "CODIGO DE BARRA ": "7792543005194",
        "DESCRIPCION DEL PRODUCTO": " Notas de Salida:\nlavanda y esclarea.\nNotas de Corazón:\ncuero, almendra amarga y vainilla\nNotas de Fondo:\ncuero haba tonka, cachemira maderas blancas y ámbar.",
        "UNIDAD DE MEDIDA": "100",
        "PESO DEL PRODUCTO": "320",
        "ATRIBUTOS DEL PRODUCTO": "EQUIVALENCIA: FUCKING FABULOUS DE TOM FORD"
        }
    ]
    contenido_perfumes = ""
    for producto in productos:
        contenido_perfumes += f"Nombre del perfume: {producto['NOMBRE DEL PRODUCTO'].strip()}\n"
        contenido_perfumes += f"Precio: {producto[' PRECIO DE VENTA EN PESOS ARGENT'].strip()}\n"
        contenido_perfumes += f"Descripción: {producto['DESCRIPCION DEL PRODUCTO'].strip()}\n"
        contenido_perfumes += f"Atributos: {producto['ATRIBUTOS DEL PRODUCTO'].strip()}\n\n"

    data = {
        "model": "deepseek/deepseek-chat:free",
        "messages": [
            {"role":"user", "content": contenido_perfumes},
            {"role": "user", "content": "como un agente de ventas sobre perfumes responde a lo siguente de la forma mas accesible posible, recuerda mencionar aspectos como el precio o la descripcion del producto"},  # Mensaje original
            {"role": "user", "content": "solo texto plano"},  # Mensaje original            
            {"role": "user", "content": texto_comparacion}  # Agregar el nuevo mensaje con texto_comparacion
        ]
    }

    response = requests.post(API_URL, json=data, headers=headers)
    data2 = response.json()

    if response.status_code == 200:
        
        print("API Response:", response.json())
        return data2['choices'][0]['message']['content']
    else:
        print("Failed to fetch data from API. Status Code:", response.status_code)
        return None
    
def send_message_wp(chat_id, text):
    """
    Send message to chat_id.
    :param chat_id: Phone number + "@c.us" suffix - 1231231231@c.us
    :param text: Message for the recipient
    """
    response = requests.post(
        WP_URL,
        json={
            "chatId": chat_id,
            "text": text,
            "session": "default",
        },
    )
    response.raise_for_status()

def send_seen_wp(chat_id, message_id, participant):
    response = requests.post(
        WP_URL,
        json={
            "session": "default",
            "chatId": chat_id,
            "messageId": message_id,
            "participant": participant,
        },
    )
    response.raise_for_status()

def procesar_mensaje_fb(msg):
    texto = msg["message"]["text"].lower()
    
    if "comparar" in texto:
        palabras = texto.split()
        if len(palabras) >=3:
            try:
                
                return generar_comparacion_ia(texto)
            except Exception as e:
                return f"Hubo un error al procesar los datos: {e}"
    
    elif "comprar" in texto:
        return "¡Claro! ¿Qué perfume te interesa comprar? Te ayudaremos con el proceso."
    
    return generar_comparacion_ia(texto)



def enviar_mensaje_facebook(user_id, texto):
    url = f"https://graph.facebook.com/v18.0/me/messages"
    headers = {"Content-Type": "application/json"}
    data = {
        "recipient": {"id": user_id},
        "message": {"text": texto},
        "messaging_type": "RESPONSE",
        "access_token": FB_ACCESS_TOKEN
    }
    requests.post(url, headers=headers, json=data)

