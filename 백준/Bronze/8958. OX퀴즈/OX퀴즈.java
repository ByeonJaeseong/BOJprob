import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String[] arr = new String[n];
		for(int i=0; i<n; i++) {
			arr[i]=sc.next();
		}
		int a=0;
		int b=0;				
		for(int i=0; i<n; i++) {
		byte[] point = arr[i].getBytes();
			for(int j=0; j<point.length; j++) {
				char c = (char) point[j];
				if(c=='O') {
					++a;
					b=b+a;
				}else {
					a=0;
				}
				
			}
			System.out.println(b);
			a=0;
			b=0;
		}

	}

}
