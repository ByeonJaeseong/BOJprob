import java.math.BigInteger;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
	      Scanner sc=new Scanner(System.in);
		        BigInteger n = sc.nextBigInteger();
		        BigInteger m = sc.nextBigInteger();
		        BigInteger a = n.divide(m);
		        BigInteger b = n.mod(m);
		        System.out.println(a);
		        System.out.println(b);
		    }
		
	}

