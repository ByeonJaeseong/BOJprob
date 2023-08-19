import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M=N;
		String[][] str = new String[N][N];
		for(int i=0; i<3; i++) {
			for(int j=0; j<3; j++) {
				if(i==1&&j==1) {
				str[i][j]=" ";}
				else {
					str[i][j]="*";
				}
			}
		}
		int a=0;
		while(N!=1) {
			N=N/3;
			a++;
		}
		int b=1;
		int c=3;
		while(b<a) {
			for(int i=0; i<c; i++) {
				for(int j=0; j<c; j++) {
					str[i+c][j]=str[i][j];
					str[i+2*c][j]=str[i][j];
					str[i][j+c]=str[i][j];
					str[i][j+2*c]=str[i][j];
					str[i+2*c][j+c]=str[i][j];
					str[i+c][j+2*c]=str[i][j];
					str[i+2*c][j+2*c]=str[i][j];
					str[i+c][j+c]=" ";
				}
			}
			c*=3;
			b++;
		}
		StringBuilder sb = new StringBuilder();
		for(int i=0; i<M; i++) {
			for (int j=0; j<M; j++) {
				sb.append(str[i][j]);
			}
			sb.append("\n");
		}
		System.out.println(sb);

	}

}
