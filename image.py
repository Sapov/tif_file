class Check_Image:
    def check_resolution(self, lst_tif, material):
        '''
        Проверяем разрешения и уменьшаем в соответствии со стандартом
        :param lst_tif:
        :param material:
        :return:
        '''
        for i in lst_tif:
            if check_tiff(i)[2] > data.propertis_material.get(material)[1]:
                print("[INFO] Разрешение больше необходимого Уменьшаем!!")
                resize_image(i, data.propertis_material.get(material)[1])
            elif check_tiff(i)[2] == data.propertis_material.get(material)[1]:
                print('[INFO] Разрешение соответствует требованиям')
            else:
                print("[INFO] Низкое разрешение не соответствует требованиям")
