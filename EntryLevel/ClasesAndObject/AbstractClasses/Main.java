class Main {
  public static void main(String args[]) {
    Moto moto = new Moto();
    Auto auto = new Auto();
    printVehicle("moto", moto);
    printVehicle("moto", auto);
  }

  public static void printVehicle(String nombre, Vehiculo vehiculo){
    System.out.println("El/La " + nombre + " tiene espacio para " + vehiculo.numOfPassagers + " pasajeros.");
    vehiculo.honk();
  }
}
