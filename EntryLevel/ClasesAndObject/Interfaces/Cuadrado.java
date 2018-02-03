public class Cuadrado implements Figura {
  private double lado;

  Cuadrado(double lado){
    this.lado = lado;
  }

  public double perimetro(){
    return this.lado*4;
  }

  public double area(){
    return this.lado*this.lado;
  }
}
