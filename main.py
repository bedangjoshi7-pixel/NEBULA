import cv2 as cv 
from pyzbar.pyzbar import decode 
import webbrowser as wb
from pysafebrowsing import SafeBrowsing

def safe_browsing(URL):
    API_Key = "Your_API_KEY"          #<--- Look at README.md on How to get your own API Key. 
    s = SafeBrowsing(API_Key)

    response = s.lookup_urls([URL])
    is_malicious = response[URL]['malicious']
    if is_malicious == False:
           wb.open_new_tab(hex_value)
    else:
        action = input("Site seems unsafe , still want to open the site ? ")
        if action in ['y','yes','yeah','yup']:
              wb.open_new_tab(hex_value)
           
    

       
capture = cv.VideoCapture(0)
while True:
            isTrue , frame = capture.read()
        
            if not  isTrue:
                print("No BarCode Detected")
            for d in decode(frame):
                    (x,y,w,h) = d.rect
                    hex_value = d.data.decode()
                    cv.rectangle(frame, (x-10, y-10),
                            (x + w+10, y + h+10), 
                            (255, 0, 0), 2)
                    print(hex_value)
                    if hex_value:
                        #    action = input("You want to Open the URL ? y/n = 'Yes/No :  ").lower()
                           safe_browsing(hex_value)
                        #    if action in ['y','yes','yup','yeah']:
                                #  wb.open_new_tab(hex_value)
            cv.imshow("WebCam",frame)
            if cv.waitKey(20) & 0xFF == ord('q'):
                break

capture.release()
cv.destroyAllWindows()






