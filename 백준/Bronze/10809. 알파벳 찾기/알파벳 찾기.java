import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String inputString =sc.next();
		
	 String[] subjects = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
			 "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};
	 for(String subject : subjects) {
	 int location = inputString.indexOf(subject);
	 System.out.print(location+" ");
	 }
			 

	}

}
