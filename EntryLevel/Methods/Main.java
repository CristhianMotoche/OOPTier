class Main {
  public static void main(String args[]) {
    MyClass.classMethod();
    MyClass myInstance = new MyClass();
    myInstance.instanceMethod();
  }
}

class MyClass {
  private static int INT = 3;
  private int simpleInt = 3;
  static void classMethod(){
    MyClass.INT = 4;
    // simpleInt cannot be assigned inside an static context
    // this.simpleInt = 4;
    System.out.println("Este método no depende de una instancia de la clase");
    System.out.println("INT ahora es: " + MyClass.INT);
  }

  public void instanceMethod(){
    this.simpleInt = 4;
    System.out.println("Este método depende de una instancia de la clase");
    System.out.println("simpleInt ahora es: " + this.simpleInt);
  }
}
