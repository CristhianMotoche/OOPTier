class Main {
  public static void main(String args[]) {
    Cuadrado cuadrado = new Cuadrado(10);
    Rectangulo rectangulo = new Rectangulo(10, 20);
    imprimirArea("Cuadrado", cuadrado);
    imprimirArea("Rectangulo", rectangulo);
  }

  public static void imprimirArea(String nombreFigura, Figura figura){
    double area = figura.area();
    System.out.println("El area del " + nombreFigura + " es " + area + " m^2");
  }
}
