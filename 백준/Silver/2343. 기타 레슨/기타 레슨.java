import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
//이분탐색 연습
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str =br.readLine();
		String[] inputNo = str.trim().split(" ");
		int N = Integer.parseInt(inputNo[0]);
		int M = Integer.parseInt(inputNo[1]);
		int sum =0;
		int[] eTime = new int[N];
		
		str=br.readLine();
		inputNo=str.trim().split(" ");
		int maxInt =0;
		for(int i=0; i<N; i++) {
			int a = Integer.parseInt(inputNo[i]);
			eTime[i]=a;
			maxInt = Math.max(maxInt, a);
			sum+=a;
		}//데이터 입력 완료
		
	
		int start =maxInt;
		int end = sum;
		int midPoint;
		while(start<=end) {
			midPoint = (start+end)/2;
		//	System.out.print(midPoint);
		//	System.out.print(" ");
			
			int bluray =1;
			int time =0;
			for(int i=0; i<N; i++) {
				time+=eTime[i];
				if(time<=midPoint) {
				}
				else {
					bluray++;
					i--;
					time=0;
				}		
			}
			//System.out.println(bluray);
			if(bluray>M) {
				start=midPoint+1;
			}else {
				end=midPoint-1;
			}
		}
		System.out.println(start);
	
	}

}
