import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] inputNo = br.readLine().trim().split(" ");
		
		int M = Integer.parseInt(inputNo[0]);
		int N = Integer.parseInt(inputNo[1]);
		long[][] input = new long[M][M];
		long[][] input_sum = new long[M][M];
		for(int i=0; i<M; i++) {
			inputNo = br.readLine().trim().split(" ");
			for(int j=0; j<M; j++) {
				input[i][j]=Long.parseLong(inputNo[j]);
				if(i!=0) {
					if(j==0) {
						input_sum[i][j]= (long) input[i][j] + input_sum[i-1][j];
					}else {						
						input_sum[i][j]=(long) input_sum[i][j-1]+input[i][j]+input_sum[i-1][j]-input_sum[i-1][j-1];
					}
				}else {
					if(j==0) {
						input_sum[i][j]= (long) input[i][j];
					}else {						
					input_sum[i][j]=(long) input_sum[i][j-1]+input[i][j];
					}
				}
						
			}
		}
		for(int i=0; i<N; i++) {
			long sum = 0;
			inputNo = br.readLine().trim().split(" ");
			int x_1 = Integer.parseInt(inputNo[0]);
			int y_1 = Integer.parseInt(inputNo[1]);
			int x_2 = Integer.parseInt(inputNo[2]);
			int y_2 = Integer.parseInt(inputNo[3]);
			if(x_1>1 && y_1>1) {
				sum = (long) input_sum[x_2-1][y_2-1]-input_sum[x_1-2][y_2-1]-input_sum[x_2-1][y_1-2]+input_sum[x_1-2][y_1-2];
				
			}else if(x_1==1 && y_1>1){
				sum = (long) input_sum[x_2-1][y_2-1]-input_sum[x_2-1][y_1-2];
				
			}else if(x_1>1 && y_1==1){
				sum = (long) input_sum[x_2-1][y_2-1]-input_sum[x_1-2][y_2-1];
			}else if(x_1==1 && y_1==1){
				sum = (long) input_sum[x_2-1][y_2-1];
			}	
					
				
			System.out.println(sum);
		}

	}

}