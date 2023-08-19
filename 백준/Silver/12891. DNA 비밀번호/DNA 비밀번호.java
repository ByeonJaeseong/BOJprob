import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		String[] number = input.trim().split(" ");
		int N = Integer.parseInt(number[0]);
		int M = Integer.parseInt(number[1]);		
		input = br.readLine();
		String pw = input;
		char[] pwChar = new char[N];
		for(int i=0; i<pw.length(); i++) {
			pwChar[i]=pw.charAt(i);
		}
		input = br.readLine();
		number = input.trim().split(" ");
		int numA = Integer.parseInt(number[0]);
		int numC = Integer.parseInt(number[1]);
		int numG = Integer.parseInt(number[2]);
		int numT = Integer.parseInt(number[3]);
		int count=0;
		int[] subPass = new int[4];
		for(int i=0; i<M; i++) {
			if(pwChar[i]=='A') {
				subPass[0]++;
			}
			if(pwChar[i]=='C') {
				subPass[1]++;
			}
			if(pwChar[i]=='G') {
				subPass[2]++;
			}
			if(pwChar[i]=='T') {
				subPass[3]++;
			}
		}
		
		for(int i=0; i<4; i++) {
			
		}
		
		for(int i=0; i+M-1<N; i++) {
			if(i==0) {
				if(subPass[0]>=numA && subPass[1]>=numC && 
						subPass[2]>=numG && subPass[3]>=numT) {
					count++;					
				}
			} else {
				if(pwChar[i-1]=='A') {
					subPass[0]--;
				}
				if(pwChar[i-1]=='C') {
					subPass[1]--;
				}
				if(pwChar[i-1]=='G') {
					subPass[2]--;
				}
				if(pwChar[i-1]=='T') {
					subPass[3]--;
				}
				
				if(pwChar[i+M-1]=='A') {
					subPass[0]++;
				}
				if(pwChar[i+M-1]=='C') {
					subPass[1]++;
				}
				if(pwChar[i+M-1]=='G') {
					subPass[2]++;
				}
				if(pwChar[i+M-1]=='T') {
					subPass[3]++;
				}
				if(subPass[0]>=numA && subPass[1]>=numC && 
						subPass[2]>=numG && subPass[3]>=numT) {
					count++;					
				}
			}
		}

		System.out.print(count);
	}

}
