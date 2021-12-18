print("***GPA 3 subject***") #เริ่ม

print("") #เว้นบรรทัดแบบคนไม่รู้

#คำนำ
print("***How to ***")
print("1.Input grade your subject (0,1,1.5,2,2.5,3,3.5,4)")
print("2.Input credit your subject (0.5,1,1.5) ")
print("*grade = เกรด (0,1,1.5,2,2.5,3,3.5,4)")
print("*credit = หน่วยกิต (0.5,1,1.5)")

print("") #เว้นบรรทัดแบบคนไม่รู้

#วิชาแรก
print("***First subject***")
grade1 = float(input("Input First subject grade:") )
credit1 = float(input("Input First subject credit:"))
#--------------------------------------------------------

print("") #เว้นบรรทัดแบบคนไม่รู้

#วิชาที่สอง
print("***Second subject***")
grade2 = float(input("Input Second subject grade:") )
credit2 = float(input("Input Second subject credit:") )
#--------------------------------------------------------

print("") #เว้นบรรทัดแบบคนไม่รู้

#วิชาที่สาม
print("***Third subject***")
grade3 = float(input("Input Third subject grade:") )
credit3 = float(input("Input Third subject credit:"))
#--------------------------------------------------------

#คำนวณเกรดที่ได้

creditall = (credit1+credit2+credit3) #รวมหน่วยกิตที่ได้

#ผลรวมของเกรด
GPA1 = (grade1*credit1) #วิชาแรก
GPA2 = (grade2*credit2) #วิชาที่สอง
GPA3 = (grade3*credit3) #วิชาที่สาม

GPAall = (GPA1+GPA2+GPA3)#

sum = (GPAall/creditall)#

sumtrue =  round(sum, 2)#ปัดเศษให้เหลือ2ตำแหน่ง

print("") #เว้นบรรทัดแบบคนไม่รู้

#แสดงเกรดเฉลี่ย
print("GPAX = ", sumtrue)

print("") #เว้นบรรทัดแบบคนไม่รู้

print("***End***") #จบ



a = input("")#ก่อนปิด





# ด.ช.เมธิชัย งอกคำ ม.210 เลขที่ 9
# ด.ช.อาดีฟ อักษร์รัตน์ ม.210 เลขที่ 13
