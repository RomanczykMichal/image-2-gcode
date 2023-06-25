import processing.svg.*;

int COLOR_WHITE = 255;
float PX_TO_MM = 0.2645;
float PEN_NOSE_MM = 2;

int STEP_IN_MM = 22;
float NOISE_SCALE = 0.03;

void setup() {
  size(220, 220, SVG, "filename.svg");
  background(COLOR_WHITE);
}

void draw() {
  //drawBoundries();
  Generator generator = new Generator1();
  generator.drawShape();
  exit();
}

void drawBoundries() {
  strokeWeight(1);
  stroke(255, 0, 0);
  line(0, 0, width, 0);
  line(width, 0, width, height);
  line(width, height, 0, height);
  line(0, height, 0, 0);
}
