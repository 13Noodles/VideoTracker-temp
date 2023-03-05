import yaml

class ColorProfile:
    def __init__(self,profileDict:dict=None) -> None:
        # default values
        self.__windowColors = {
            "background":"black"
        }
        self.__buttonColors = {
            "text":"black",
            "border":"lightgray",
            "background":"lightgray",
            "backgroundOver":"gray"
        }
        self.__labelColors = {
            "text":"black",
            "background":"lightgray"
        }
        self.__entryColors = {
            "text":"black",
            "background":"lightgray"
        }
        self.__name = "nameUnspecified"
        
        # if dict provided, overwrite the defaults
        if(profileDict != None):
            self.initFromDict(profileDict)
    

    ##############################
    #       INITIALIZERS         #
    ##############################
    def initFromFile(self, path:str) -> int:
        with open(path) as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            self.initFromDict(config)

    def initFromDict(self, profileDict: dict):
        
        # init profile name
        if("name" in profileDict):
            self.__name = profileDict["name"]
        else:
            print(f"WARN profile init : name not specified, keeping default value")
        # init window colors
        if("window" in profileDict):
            for key in self.__windowColors.keys():
                if(key in profileDict["window"]):
                    self.__windowColors[key] = profileDict["window"][key]
                else:
                    print(f"WARN profile init (name:'{self.__name}'): window:{key} not specified, keeping default value")
        else:
            print(f"WARN profile init (name:'{self.__name}'): window not specified, keeping default value")

        # init button colors
        if("button" in profileDict):
            for key in self.__buttonColors.keys():
                if(key in profileDict["button"]):
                    self.__buttonColors[key] = profileDict["button"][key]
                else:
                    print(f"WARN profile init (name:'{self.__name}'): button:{key} not specified, keeping default value")
        else:
            print(f"WARN profile init (name:'{self.__name}'): button not specified, keeping default value")
        
        # init label colors
        if("label" in profileDict):
            for key in self.__labelColors.keys():
                if(key in profileDict["label"]):
                    self.__labelColors[key] = profileDict["label"][key]
                else:
                    print(f"WARN profile init (name:'{self.__name}'): label:{key} not specified, keeping default value")
        else:
            print(f"WARN profile init (name:'{self.__name}'): label not specified, keeping default value")
        # init label colors
        if("entry" in profileDict):
            for key in self.__entryColors.keys():
                if(key in profileDict["label"]):
                    self.__entryColors[key] = profileDict["entry"][key]
                else:
                    print(f"WARN profile init (name:'{self.__name}'): entry:{key} not specified, keeping default value")
        else:
            print(f"WARN profile init (name:'{self.__name}'): entry not specified, keeping default value")
        

    ##############################
    #            ETC             #
    ##############################
    def __str__(self) -> str:
        data = {
            "name":self.__name,
            "window":self.__windowColors,
            "button":self.__buttonColors,
            "label":self.__labelColors,
            "entry":self.__entryColors
        }
        return str(data)

    def name(self) -> str:
        return self.__name


    ##############################
    #   WINDOW COLORS GETTERS    #
    ##############################
    def windowColors(self) -> dict:
        return self.windowColors
    def windowBackground(self) -> str:
        return self.__windowColors["background"]


    ##############################
    #   BUTTONS COLORS GETTERS   #
    ##############################
    def buttonColors(self) -> dict:
        return self.__buttonColors
    def buttonBorder(self) -> str:
        return self.__buttonColors["border"]
    def buttonText(self) -> str:
        return self.__buttonColors["text"]
    def buttonBackground(self) -> str:
        return self.__buttonColors["background"]
    def buttonBackgroundOver(self) -> str:
        return self.__buttonColors["backgroundOver"]


    ##############################
    #   LABELS COLORS GETTERS    #
    ##############################
    def labelColors(self) -> dict:
        return self.__labelColors
    def labelText(self) -> str:
        return self.__labelColors["text"]
    def labelBackground(self) -> str:
        return self.__labelColors["background"]


    ##############################
    #   ENTRIES COLORS GETTERS   #
    ##############################
    def entryColors(self) -> dict:
        return self.__entryColors
    def entryText(self) -> str:
        return self.__entryColors["text"]
    def entryBackground(self) -> str:
        return self.__entryColors["background"]