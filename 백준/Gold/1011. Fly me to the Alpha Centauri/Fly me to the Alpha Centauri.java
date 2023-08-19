import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int finish = 0;
		while(finish<N) {
			long start = sc.nextLong();
			long end = sc.nextLong();
			long dis = (long) end - start;
			long i = 0;
			while(true) {
				if((long)i*i-i<dis && dis <=(long)i*i) {
					System.out.println(2*i-1);
					break;
				}
				if((long)i*i<dis && dis <=(long)i*i+i) {
					System.out.println(2*i);
					break;
				}
				i++;
			}
			finish++;
		}

	}

}
