class BadSemantics {
  public static void main(String args[]) {
    System.out.println("Factorial(0) = " + BadSemantics.factorial(0));
    System.out.println("Factorial(1) = " + BadSemantics.factorial(1));
    System.out.println("Factorial(2) = " + BadSemantics.factorial(2));
    System.out.println("Factorial(3) = " + BadSemantics.factorial(3));
  }

  // El siguiente método tiene la sintaxis de Java correcta.
  // Sin embargo, el condicional está incorrecto para cumplir con el método factorial.
  // Este problema generará un error de StackOverflow.
  static long factorial(int n) {
    if (n > 1) {
      return 1;
    }
    return n*factorial(n - 1);
  }
}
