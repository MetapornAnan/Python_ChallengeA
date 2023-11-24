from area import rec_area,cir_area,prism_vol,sphere_vol
from lookbak import rectangle_vol as cube_rec_vol,sphere_vol as cube_sphere_vol

def main():
    print('-------------------------- Area & Cube -------------------------------')
    print('1.พื้นที่สี่เหลี่ยม 2.พื้นที่วงกลม 3.ปริมาตรทรงสี่เหลี่ยม 4.ปริมาตรทรงกลม 0.ออกจากการทำงาน')

    while True:
        try:
            choice = int(input('---------------------\nเลือกเมนู : '))
            print('------------------------------------------')

            if choice == 0:
                print('-------------------------\nทำความรู้จบ\n--------------------')
                break
            elif choice in [1, 2, 3, 4]:
                if choice == 1:
                    width = float(input('ป้อนความกว้าง :'))
                    length = float(input('ป้อนความยาว :'))
                    print(f"พื้นที่สี่เหลี่ยม: {rec_area(width, length)}")
                elif choice == 2:
                    radius = float(input('ป้อนรัศมี: '))
                    print(f"พื้นที่วงกลม: {cir_area(radius)}")
                elif choice == 3:
                    width = float(input("ป้อนความกว้าง: "))
                    length = float(input("ป้อนความยาว: "))
                    height = float(input("ป้อนความสูง: "))
                    print(f"ปริมาตรทรงสี่เหลี่ยม: {prism_vol(width, length, height)}")
                elif choice == 4:
                    radius = float(input("ป้อนรัศมี: "))
                    print(f"ปริมาตรทรงกลม: {sphere_vol(radius)}")
            else:
                print("-----------------------\nกรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น\n-----------------------")
        except ValueError:
            print("--------------------------------\nกรุณาป้อนตัวเลขเท่านั้น\n--------------------------------")

if __name__ == "__main__":
    main()