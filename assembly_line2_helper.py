import os
recipe = {#key:material value:[price,[recipe1,recipe2,...],[number1,number2]]
    'Aluminium' : [80],
    'Copper' : [80],
    'Diamond' : [80],
    'Gold' : [80],
    'Iron' : [80],
    'Plutonium' : [4000],
    'Uranium' : [4000],
    'Aluminium_Wire' : [150,['Aluminium'],[1]],
    'Copper_Wire' : [150,['Copper'],[1]],
    'Diamond_Wire' : [150,['Diamond'],[1]],
    'Gold_Wire' : [150,['Gold'],[1]],
    'Iron_Wire' : [150,['Iron'],[1]],
    'Aluminium_Gear' : [200,['Aluminium'],[1]],
    'Copper_Gear' : [200,['Copper'],[1]],
    'Diamond_Gear' : [200,['Diamond'],[1]],
    'Gold_Gear' : [200,['Gold'],[1]],
    'Iron_Gear' : [200,['Iron'],[1]],
    'Aluminium_Liquid' : [200,['Aluminium'],[1]],
    'Copper_Liquid' : [200,['Copper'],[1]],
    'Diamond_Liquid' : [200,['Diamond'],[1]],
    'Gold_Liquid' : [200,['Gold'],[1]],
    'Iron_Liquid' : [200,['Iron'],[1]],
    'Server_Rack' : [320,['Aluminium','Iron'],[1,1]],
    'Aluminium_Plate' : [350,['Aluminium'],[1]],
    'Copper_Plate' : [350,['Copper'],[1]],
    'Diamond_Plate' : [350,['Diamond'],[1]],
    'Gold_Plate' : [350,['Gold'],[1]],
    'Iron_Plate' : [350,['Iron'],[1]],
    'Circuit' : [460,['Copper_Wire','Gold'],[1,1]],
    'Electric_Board' : [460,['Copper_Wire','Aluminium'],[1,1]],
    'Heater_Plate' : [460,['Iron_Wire','Aluminium'],[1,1]],
    'Battery' : [560,['Copper_Liquid','Copper'],[1,1]],
    'Engine' : [560,['Iron_Gear','Iron'],[1,1]],
    'Solar_Cell' : [560,['Diamond_Liquid','Gold'],[1,1]],
    'Aluminium_Cable' : [600,['Aluminium_Wire'],[3]],
    'Copper_Cable' : [600,['Copper_Wire'],[3]],
    'Diamond_Cable' : [600,['Diamond_Wire'],[3]],
    'Gold_Cable' : [600,['Gold_Wire'],[3]],
    'Iron_Cable' : [600,['Iron_Wire'],[3]],
    'Processor' : [4530,['Circuit','Gold_Liquid','Diamond_Wire'],[1,3,3]],
    'Fan' : [4620,['Circuit','Diamond_Gear','Aluminium'],[1,3,6]],
    'Power_Supply' : [4620,['Circuit','Diamond','Aluminium_Liquid'],[1,6,3]],
    'Solar_Panel' : [7500,['Solar_Cell','Circuit','Electric_Board'],[2,1,2]],
    'Plutonium_Refined' : [12000,['Plutonium'],[1]],
    'Uranium_Refined' : [12000,['Uranium'],[1]],
    'Advanced_Engine' : [17700,['Engine','Circuit','Diamond'],[5,5,10]],
    'Laser' : [18300,['Battery','Heater_Plate','Iron_Liquid'],[5,5,5]],
    'Computer' : [41310,['Fan','Power_Supply','Processor'],[1,1,1]],
    'Explosive' : [55600,['Circuit','Diamond_Wire','Copper_Cable','Heater_Plate'],[5,10,10,10]],
    'Trigger' : [66800,['Iron','Diamond_Wire','Circuit','Electric_Board'],[40,10,5,5]],
    'Plutonium_Cell' : [137200,['Plutonium','Solar_Cell','Diamond_Liquid','Gold_Cable','Copper_Cable'],[2,2,2,2,2]],
    'Uranium_Cell' : [137200,['Uranium','Solar_Cell','Diamond_Liquid','Gold_Cable','Copper_Cable'],[2,2,2,2,2]],
    'Plutonium_Circuit' : [83440,['Plutonium','Circuit','Copper','Gold_Cable','Diamond_Wire'],[4,5,5,1,2]],
    'Uranium_Circuit' : [83440,['Uranium','Circuit','Copper','Gold_Cable','Diamond_Wire'],[4,5,5,1,2]],
    'Electric_Engine' : [156760,['Battery','Advanced_Engine','Electric_Board','Iron_Plate'],[2,2,2,5]],
    'AI_Robot_Arms' : [158960,['Laser','Aluminium_Plate','Aluminium_Cable','Iron'],[2,2,3,8]],
    'Super_Computer' : [344480,['Computer','Server_Rack','Circuit','Gold_Cable'],[2,1,3,3]],
    'Nuclear_Cell' : [int(1.19e6),['Uranium_Cell','Plutonium_Cell','Solar_Cell','Electric_Board','Heater_Plate'],[1,1,3,3,3]],
    'AI_Robot_Body' : [int(1.33e6),['Electric_Engine','Solar_Panel','AI_Robot_Arms','Electric_Board'],[1,2,1,5]],
    'AI_Processor' : [int(1.41e6),['Circuit','Super_Computer','Copper_Plate','Copper_Cable'],[10,1,6,4]],
    'Nuclear_Circuit' : [int(2.03e6),['Uranium_Circuit','Plutonium_Circuit','Circuit','Gold_Cable','Processor'],[1,1,3,3,3]],
    'AI_Robot_Head' : [int(5.7e6),['AI_Processor','Gold_Plate','Diamond_Cable','Circuit'],[1,5,10,10]],
    'Ignition_System' : [int(13.1e6),['Trigger','Explosive','AI_Processor','Battery'],[2,5,2,5]],
    'Nuclear_Core' : [int(12.74e6),['Nuclear_Cell','Uranium_Cell','Plutonium_Cell','Processor','Diamond_Cable','Gold_Cable'],[1,1,1,10,4,4]],
    'AI_Robot' : [int(28.18e6),['AI_Robot_Body','AI_Robot_Head','Iron_Plate','Diamond_Cable'],[1,1,10,5]],
    'Nuclear_Processor' : [int(33.77e6),['Nuclear_Circuit','Uranium_Circuit','Plutonium_Circuit','AI_Processor','Processor','Diamond_Plate'],[1,1,1,1,5,10]],
    'Atomic_Bomb' : [int(548.54e6),['Nuclear_Processor','Nuclear_Core','Ignition_System','Nuclear_Cell','Uranium','Plutonium'],[1,1,1,1,15,15]],
    'AI_Robot_Bomber' : [int(5.6e9),['Atomic_Bomb','AI_Robot','AI_Processor','Nuclear_Cell','Nuclear_Processor','Nuclear_Circuit'],[1,1,2,3,1,3]]
}

def check_name():
    """
    检查笨蛋作者的拼写错误
    """
    flag = False
    for v in recipe.keys():
        if len(recipe[v]) != 1:
            for name in recipe[v][1]:
                if name not in recipe or len(recipe[v][1]) != len(recipe[v][2]):
                    print(v,name)
                    flag = True
    if not flag:print("All names of recipes are correct!")

def print_path(name:str,n = 1,flag = True,prefix = '',flag2 = True,importer = [])-> dict:
    """
    打印物品的生产路径。
    :name:物品名称
    """
    if name not in recipe:
        print('Please check your input.\nNames must be the same with them in recipe!')
        return {}
    count = dict()
    for k in recipe:
        count[k] = 0
    count[name] += n
    if flag2:
        print(prefix + '{} {}'.format(round(n,3),name))
    if len(recipe[name]) == 1:
        return count
    l = len(recipe[name][1])
    for i in range(l):
        son_prefix = prefix.replace('└',' ').replace('├','|') + ('├' if i < l - 1 else '└')
        if recipe[name][1][i] not in importer:
            son_count = print_path(recipe[name][1][i],recipe[name][2][i] * n,flag = False,prefix = son_prefix,flag2 = flag2)
            for key in son_count:
                count[key] += son_count[key]
        else:print(son_prefix+str(recipe[name][2][i] * n),recipe[name][1][i],'--'*5)
    if flag:
        for key in count:
            if count[key] > 0:print('{} {}'.format(key.rjust(20),str(round(count[key],3)).rjust(3)))
    return count

def design_line(name:str,n = 1):
    #根据物品的生产路径统计设计总线式生产线的顺序
    count = print_path(name,n,flag = False,flag2 = False)
    for k in count.keys():
        if count[k] != 0:
            if len(recipe[k]) == 1:
                print('+{} {}'.format(str(round(count[k],3)).ljust(5),k.rjust(20)))
            else:
                for i in range(len(recipe[k][1])):
                    count[recipe[k][1][i]] -= count[k] * recipe[k][2][i]
                    print('-{} {} ({} left)'.format(str(round(count[k] * recipe[k][2][i],3)).ljust(5),recipe[k][1][i].rjust(20),round(count[recipe[k][1][i]],3)))
                print('+{} {}'.format(str(round(count[k],3)).ljust(5),k.rjust(20)))

def print_raw(name,flag = True) -> dict:
    """
    打印并返回物品的原材料
    :name:物品名称
    :flag:是否打印
    """
    if name not in recipe:
        print('Please check your input.\nNames must be the same with them in recipe!')
        return []
    count = {
    'Aluminium' : 0,
    'Copper' : 0,
    'Diamond' : 0,
    'Gold' : 0,
    'Iron' : 0,
    'Plutonium' : 0,
    'Uranium' : 0
    }
    if name not in count:
        for i in range(len(recipe[name][1])):
            if recipe[name][1][i] not in count:
                tmp = print_raw(recipe[name][1][i],flag = False)
                for tmpkey in tmp:
                    count[tmpkey] += tmp[tmpkey] * recipe[name][2][i]
            else:
                count[recipe[name][1][i]] += recipe[name][2][i]
    else:count[name] = 1
    
    if flag:
        for key in count:
            print('{} {}'.format(key.rjust(20),str(round(count[key],2)).rjust(3)))
    return count

def sort_worth():
    """
    对全部物品的单位价值排序，并打印。
    """
    material = []#[[名称,原料总数,单价,单位原料价格]]
    for k in recipe:
        tmp = print_raw(k,flag = False)
        n_resource = sum(tmp.values()) - tmp['Plutonium'] - tmp['Uranium']
        material.append([k,n_resource,recipe[k][0],recipe[k][0]/(n_resource if n_resource > 0 else 1)])
    material.sort(key = lambda x:x[3])
    print('{} {} {} {}'.format('Name'.rjust(20),'Raw'.rjust(6),'Price'.rjust(15),'Price/Raw'.rjust(10)))
    for m in material:
        print('{} {} {} {}'.format(m[0].rjust(20),str(m[1]).rjust(6),str(m[2]).rjust(15),str(int(m[3])).rjust(10)))

if __name__ == '__main__':
    message = '''Press 'q'+'Enter' to quit.
Input 's'+'Enter' to know materials' value.
Input 'r'+'Enter' to get recipe.
Input 'p'+'name'(+'number')+'Enter' to get production path. Example: 'p Solar_Cell 6'+'Enter'
Input 'd'+'name'(+'number')+'Enter' to design production path. Example: 'd Solar_Cell 6'+'Enter'
Names must be the same with them in recipe!
Press 't'+'Enter' to see this tip again.'''
    print(message)
    while(True):
        try:
            tmp = list(map(str,input().strip().split()))
            os.system('cls')
            if tmp[0] == 'q':
                break
            elif tmp[0] == 'r':
                for key in recipe:
                    print(key)
            elif tmp[0] == 's':
                sort_worth()
            elif tmp[0] == 'p':
                print(tmp[1])
                if len(tmp) == 3:
                    exec('print_path(tmp[1],n='+tmp[2]+')')
                if len(tmp) > 3:
                    importer = tmp[3:]
                    
                    exec('print_path(tmp[1],n='+tmp[2]+',importer = importer)')
                else:print_path(tmp[1])
            elif tmp[0] == 'd':
                print(tmp[1])
                if len(tmp) > 2:
                    exec('design_line(tmp[1],n='+tmp[2]+')')
                else:design_line(tmp[1])
            else:
                print(message)
        except:
            pass