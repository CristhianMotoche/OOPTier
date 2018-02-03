class Rectangulo implements Figura {
  private double ladoMenor;
  private double ladoMayor;

  Rectangulo(double ladoMenor, double ladoMayor){
    this.ladoMenor = ladoMenor;
    this.ladoMayor = ladoMayor;
  }

  public double perimetro(){
    return 2*(this.ladoMenor + this.ladoMayor);
  }

  public double area(){
    return this.ladoMenor*this.ladoMayor;
  }
}
