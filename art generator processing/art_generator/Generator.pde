abstract class Generator {

  public void drawShape(){};
  
  public void setupShape() {
    stroke(0);
    strokeWeight(PX_TO_MM * PEN_NOSE_MM);
    noFill();
  }
}
