class Generator1 extends Generator {

  public void drawShape() {
    setupShape();
    float rootLength = 40;
    for (int row = STEP_IN_MM; row < height - STEP_IN_MM; row++) {
      if (row % 3 == 0) {
        float x = 0, noiseVal = 0;
        float y = map(row, STEP_IN_MM, height - STEP_IN_MM, STEP_IN_MM, STEP_IN_MM + rootLength);
        beginShape();
        curveVertex(0, y);
        curveVertex(STEP_IN_MM, y);
        for (int i = 2; i <= width / STEP_IN_MM && i * STEP_IN_MM <= width - STEP_IN_MM; i++) {
          noiseVal = map(noise(i * NOISE_SCALE * (row * 0.06), y * NOISE_SCALE), 0, 1, 0, 3);
          x = i * STEP_IN_MM;
          y = y + (noiseVal * y*0.1 * (rootLength) * NOISE_SCALE);
          curveVertex(x, y);
        }
        curveVertex(width, y);
        endShape();
      }
    }
  }
}
