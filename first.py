class Router:
    '''Router class'''
       
    def _init_(self, model, swversion, ip_add):
        '''initialise self values'''
        self.model=model
        self.swversion=swversion
        self.ip_add=ip_add            
       
    def getdesc(self):
        '''returns a formated description of arouter'''
        desc = f'Router Model             :{self.model}\n'\
               f'Software Version         :{self.swversion}\n'\
               f'Router Management Address:{self.ip_add}'
        return desc
        
        rtr1 = Router('iosV', '15.6.7', '10.10.10.1')
        rtr2 = Router('isr4221', '16.9.5', '10.10.10.5')
    print('rtr1\n', rtr1.getdesc(), '\n', sep='')
    print('rtr2\n', rtr2.getdesc(), sep='')