# Sehat - Complete Healthcare Solution

 Sehat is an application where you can check your health from anywhere around the globe. It offers various features such as:-

1. Medical Test which includes Heart rate, Oxygen saturation rate, Blood Pressure, Respirational rate and all vital signs and all these test you can complete by using your phone from anywhere & anytime.
2. Sehat also gives free cost estimation application where you can find the aproximate cost for the treatment of any disease.
3. The web application provides a platform to search nearby Hospitals, Atm's, Pharmacy etc. 
4. It also offers you to check your nutitional diet daily. Apart from this Sehat is fully secured application with high accuracy.
5. therefore, By using Sehat you can reduce the cost of your treatment by more than half.

## How the Medical Test Process works:-
A preview for 30 seconds of recording will be processed frame by frame to get the intensities of RBG colors on each frame.

## (Heart rate)

Red and Green intensities will be stored in an array that will be applied on a Fast Fourier Transform, on the resultant array the highest peak after neglecting the noise which will be on the first few stored data will contain the frequency of the heart rate on 1 second, after that the heart beat will be estimated. (Fft)

## (Blood pressure)

After estimating the heart rate, blood pressure can be estimated by using some equation which will be mentioned in the references.

## (Respiration Rate)

Same as Heart Rate, the difference is a bandpass filter must be applied from 0.1 Hz to 0.4Hz with 0.2Hz center frequency to get the Respiration rate. (Fft2)

## (Oxygen Saturation Level)

Ac and Dc signals must be obtained from the PPG signal. Dc signal is the mean values of the Red and Blue intensities for the whole period of time, while the Ac Signal is the Standard Deviation and it can be calculated as follows from here : https://en.wikipedia.org/wiki/Standard_deviation

## Nutrition Diet:-
   In the Website we have included a special nutrition diet chart, that gives us the amount of nutrition which is decided according to the given data submitted by an individual which includes Age,weight and height.
   It also gives us the information about the vitamins and minerals consumed in a day,by the amount of food taken in that particular day

## Hospital Way Finder:-
   The web application provides a platform to search nearby Hospitals, Atm's, Pharmacy etc. Using the map you can find the places.
   
## Cost Estimation Prediction:-
   Sehat also gives free cost estimation application where you can find the aproximate cost for the treatment of any disease. It is implemented using Python. 
  

ِApplication Apk for testing
Direct Link to download the Application to test it: https://drive.google.com/drive/folders/1FyJYI-JWxMN-4IMerb9d9eeO6PmlYBEH?usp=sharing

Website Link - https://sehatcompletehealthcare.000webhostapp.com
