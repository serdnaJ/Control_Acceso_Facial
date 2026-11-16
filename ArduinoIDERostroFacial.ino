const int ledVerde = 6;
const int ledRojo = 10;
const int ledAmarillo = 9;
char datoSerial;

void setup() {
  Serial.begin(9600); // Inicia comunicación serial a 9600 baudios
  pinMode(ledVerde, OUTPUT);
  pinMode(ledRojo, OUTPUT);
  pinMode(ledAmarillo, OUTPUT);
  
  // Estado inicial: ambos apagados
  digitalWrite(ledVerde, LOW);
  digitalWrite(ledRojo, LOW);
  digitalWrite(ledAmarillo, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    datoSerial = Serial.read(); // Lee el carácter enviado por Python

    if (datoSerial == '1') {
      // Rostro detectado: Acceso correcto
      digitalWrite(ledVerde, HIGH);
      digitalWrite(ledRojo, LOW);
    } 
    else if (datoSerial == '0') {
      // Sin rostro: Acceso denegado
      digitalWrite(ledVerde, LOW);
      digitalWrite(ledRojo, HIGH);
    }
  }
}