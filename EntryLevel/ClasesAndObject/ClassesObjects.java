class Classes {
  public static void main(String args[]) {
    /* Objeto */
    Caballo rocinante = new Caballo("Rocinante");
    rocinante.relinchar();
  }
}

/* Clase */
class Caballo {
  /* Atributos */
  public String nombre;
  private int edad;
  private double peso;
  private double tamanio;

  /* Métodos */
  // Constructor
  Caballo(String nombre) {
    this.nombre = nombre;
  }

  public void relinchar(){
    System.out.println(this.nombre + " está relinchando");
  }
}
