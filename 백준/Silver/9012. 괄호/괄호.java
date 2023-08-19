import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		String[] input = new String[N];
		for(int i=0; i<input.length;i++) {
			input[i]=sc.next();
		}
		for(int i=0; i<input.length;i++) {
			int a=0;
			int b=0;
			int c=0;
			for(int j=0; j<input[i].length();j++) {
				if(input[i].charAt(j)=='(') {
					a++;
				}else {
					b++;
				}
				if(a<b) {
					System.out.println("NO");
					c++;
					break;
				}
			}
			if((c==0)&&(a==b)) {
				System.out.println("YES");
			}else if((c==0)&&(a!=b)) {
				System.out.println("NO");
			}
		}

	}

}