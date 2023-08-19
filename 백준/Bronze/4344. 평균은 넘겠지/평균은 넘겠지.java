import java.text.DecimalFormat;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int C = sc.nextInt();
		double a=0;
		double b=0;
		int c=0;
		for(int i=0; i<C; i++) {
			int N=sc.nextInt();
			int[] arr= new int[N];
			for(int k=0; k<N; k++) {
				arr[k]=sc.nextInt();
			}
			for(int j=0; j<N; j++) {
				a = (double) a+arr[j];
			}
			b= (double) a/N;
			for(int l=0; l<N;l++) {
				if(arr[l]>b) {
					c++;
				}
			}
			double e = (double)c/(double)N;
			double d = Math.round(e*100000)/(double)1000;
			DecimalFormat df = new DecimalFormat("0.000");
			System.out.println(df.format(d)+"%");
			a=0;
			b=0;
			c=0;
		}
	}

}