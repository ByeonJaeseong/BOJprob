import java.math.BigInteger;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		BigInteger M =sc.nextBigInteger();
		BigInteger N =sc.nextBigInteger();
		
		System.out.println(M.add(N));
		System.out.println(M.subtract(N));
		System.out.println(M.multiply(N));

	}

}
