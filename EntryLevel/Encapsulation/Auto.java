class Auto {
  private static final int MAX_GAS_LEVEL = 500;
  private static final int LITROS_POR_KILOMETRO = 5;
  private boolean isOn;
  private int nivelGasolina;

  Auto(){
    this.isOn = false;
    this.nivelGasolina = 100;
  }

  public boolean tieneGasolina(){
    return this.nivelGasolina > 0;
  }

  public void turnOn(){
    if (this.nivelGasolina > 0) {
      this.isOn = false;
    }

    this.isOn = true;
  }

  public void turnOff(){
    this.isOn = false;
  }

  public void llenarTanque(int gasolinaParaElTanque) {
    if (this.nivelGasolina + gasolinaParaElTanque > Auto.MAX_GAS_LEVEL) {
      this.nivelGasolina = Auto.MAX_GAS_LEVEL;
      return;
    }

    this.nivelGasolina += gasolinaParaElTanque;
  }

  public void mover(int kilometros) {
    if (!this.isOn || this.nivelGasolina == 0) {
      System.out.println("El auto está apagado o no tiene gasolina");
      return;
    }

    int tmpGasto = this.calculoGastoGasolina(kilometros);
    if (tmpGasto > this.nivelGasolina) {
      System.out.println("El auto no se movio por falta de gasolina");
      return;
    }

    this.nivelGasolina -= tmpGasto;
    System.out.println("El auto se movió. Ahora tiene: " + this.nivelGasolina + "lt");
  }

  private int calculoGastoGasolina(int kilometros){
    return Auto.LITROS_POR_KILOMETRO*kilometros;
  }
}
