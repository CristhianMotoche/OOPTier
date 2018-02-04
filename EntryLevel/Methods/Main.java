class Main {
  public static void main(String args[]) {
    MyClass.classMethod();
    MyClass myInstance = new MyClass();
    myInstance.instanceMethod();
  }
}

class MyClass {
  static void classMethod(){
    System.out.println("Este método no depende de una instancia de la clase");
  }

  public void instanceMethod(){
    System.out.println("Este método depende de una instancia de la clase");
  }
}
