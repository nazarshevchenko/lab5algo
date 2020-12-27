
class BoyerMoore:
    
    def __init__(self, wanted_tape: str):
        
        if not isinstance(wanted_tape, str):
            raise TypeError

        self.wanted_tape  = wanted_tape
        self.__create_image_tape()


    def find_in(self, full_tape: str):


        if not isinstance(full_tape, str):
            raise TypeError
        
        wanted_tape = self.wanted_tape
        full_tape = list(full_tape)

        lengths_wanted_tape  = len(self.wanted_tape)
        lengths_full_tape    = len(full_tape)

        if lengths_wanted_tape > lengths_full_tape:
            return []

        i = lengths_wanted_tape - 1
        
        def get_step(obj, i):
            
            result = 0

            if obj in self.unique_symbols:

                if not (i + self.unique_symbols[obj]) > lengths_full_tape:
                    i += self.unique_symbols[obj]
                    result = i
            

                    
            else:
                if not (i + self.unique_symbols["*"]) > lengths_full_tape:
                    i += self.unique_symbols["*"]
                    result = i


            return result


        result = []
        while True:
        
            if full_tape[i] == wanted_tape[-1]:
                evaluation_tape = full_tape[(i + 1 - lengths_wanted_tape) : i+1]
                if evaluation_tape == list(wanted_tape):
                    result.append(i + 1 - lengths_wanted_tape)
                    j = get_step(full_tape[i], i)
                    if not j or j >= lengths_full_tape:
                        break

                    i = j

                else:
                    j = get_step(full_tape[i], i)
                    if not j or j >= lengths_full_tape:
                        break

                    i = j
            
            else:
                
                j = get_step(full_tape[i], i)
                if not j or j >= lengths_full_tape:
                    break
                i = j

        return result
                


                    
    
    def __create_image_tape(self):
        image = list(self.wanted_tape) 
        image.reverse()                 # reverse wanted tape for convenience
        
        
        modified_image = image[1::]
        unique_symbols = {}
        
        index = 1
        for i in modified_image:
            if i not in unique_symbols:
                unique_symbols[i] = index
            index += 1
        
        if image[0] not in unique_symbols:
            unique_symbols[image[0]] = index
        
        unique_symbols["*"] = index 
        
        self.unique_symbols = unique_symbols
    
    

