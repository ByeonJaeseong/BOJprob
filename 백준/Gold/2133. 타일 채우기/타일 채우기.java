import java.util.Scanner;

public class  Main{

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long[] data = new long[31];
		data[0]=1;
		for(int i=2; i<=30; i=i+2) {
			data[i]=3*data[i-2];
			for(int j=i-4; j>=0; j=j-2) {
				data[i]+=2*data[j];
			}
		}
		System.out.println(data[N]);

	}

}
