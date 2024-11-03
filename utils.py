from PIL import Image
import pytesseract
import re
#import mysql.connector
import cv2
import os


#image_type='pan'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#image_path = 'aadhar.png'
def imagetext(img):
  #img = cv2.imread(image_path)
  text = pytesseract.image_to_string(img)
  all_text_list = re.split(r'[\n]', text)
  print(all_text_list);

  name_pattern = r"[^a-zA-Z0-9\s]"
  dob_pattern = r"(?:\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|\d{4}\/\d{2}\/\d{2})"

  type = '';
  name = '';
  dob = '';
  father_name = 'NA';

  if 'TAX' in all_text_list[0]:
    type = "Pan Card"
  elif 'INDIA' in all_text_list[0]:
    type = "Aadhar Card"
  else:
    type = "Aadhar Card"

  print(type);

  if type == "Aadhar Card":
    name = re.sub(name_pattern, '', all_text_list[1]);
    dob = re.findall(dob_pattern, all_text_list[3])[0]
    if not dob:
      dob = re.findall(r'\d+', all_text_list[3])[0]
  elif type == 'Pan Card':
    name = re.sub(name_pattern, '', all_text_list[1]);
    father_name = re.sub(name_pattern, '', all_text_list[3]);
    dob = re.findall(dob_pattern, all_text_list[5])
  if not dob:
      dob = re.findall(r'\d+', all_text_list[5])[0]

  print(name);
  print(dob);
  print(father_name);
  arr = [name, dob, father_name, type];
  return arr

  '''
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Anushannu@2005"
  )
  mydb.database='anudb'
  mycursor = mydb.cursor()

  sql = "INSERT INTO visi_OCR (name, dob, father_name, card_type) VALUES (%s, %s,%s,%s)"
  val = (name, dob, father_name,type)
  mycursor.execute(sql, val)

  mydb.commit()
  mydb.close()
  '''