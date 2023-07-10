int voltage_offset = 20;// set the correction offset value
//const int sensorIn = 34;      // pin where the OUT pin from sensor is connected on Arduino
int mVperAmp = 185;           // this the 5A version of the ACS712 -use 100 for 20A Module and 66 for 30A Modul
void setup() {
  // Robojax.com voltage sensor
  Serial.begin(115200);
}

void loop() {

int voltage = getVoltage();
int current = getCurrent();

  int power = voltage*current;
  Serial.print("Power : ");
  Serial.print(power);
}

int getVoltage(){
  int volt = analogRead(34);// read the input - GPIO_NUM_34
  double voltage = map(volt,0, 4096, 0, 1650) + voltage_offset;

  voltage /= 100; // divide by 100 to get the decimal values
  Serial.print("Voltage: ");
  Serial.print(voltage);
  Serial.println("V");
  delay(500);
  return voltage;

  }

  int getCurrent()
  {
   int Voltage = getVoltage();
   int VRMS = (Voltage/2.0) *0.707;   //root 2 is 0.707
   int current = ((VRMS * 1000)/mVperAmp);

   return current;
  }
  
