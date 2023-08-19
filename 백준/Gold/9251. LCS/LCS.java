import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] inputStr = str.trim().split("");
		int N = inputStr.length;// 세로 길이
		str = br.readLine();
		String[] inputStr2 = str.trim().split("");
		int M = inputStr2.length;//가로길이
		int[][] LCS = new int[N][M];
		for(int i = 0; i<N; i++) {
			String a = inputStr[i];
			int Max =0 ;
			for(int j=0; j<M; j++) {
								
				if(i==0&&a.equals(inputStr2[j])) {
					LCS[i][j]++;
				}else if(i!=0) {
					if(a.equals(inputStr2[j])) {
					LCS[i][j]=Max+1;}
					else {
						LCS[i][j]=LCS[i-1][j];
					}
				}
				if(i!=0) {
					Max = Math.max(Max, LCS[i-1][j]);
				//	System.out.println(Max);
				}
				
				
			}
		}
		int Max=0;
//		for(int i=0; i<N; i++) {
//			for(int j=0; j<M; j++) {
//				System.out.print((LCS[i][j])+" ");
//			}
//			System.out.println();
//		}
		
		for(int i=0; i<M; i++) {
			Max=Math.max(Max, LCS[N-1][i]);
		}
		System.out.print(Max);
		

	}

}
