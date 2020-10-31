import java.io.IOException;
import java.util.StringTokenizer;
import java.util.HashMap;
// import java.lang.String;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class HadoopWordCountSample {
    public static class WordCountMapper
            extends Mapper<Object, Text, Text, IntWritable>{

        private final static IntWritable plugOne  = new IntWritable(1);
        private Text word = new Text();
        private HashMap<String, String> monthDict = new HashMap<String, String>();
        private String time;
        private String hour;
        private String date;
        private String month;
        private String year;

        @Override
        public void map(Object key, Text value, Context context
        ) throws IOException, InterruptedException {
			      /* Init monthDict */
            monthDict.put("Jan", "01");
            monthDict.put("Feb", "02");
            monthDict.put("Mar", "03");
            monthDict.put("Apr", "04");
            monthDict.put("May", "05");
            monthDict.put("Jun", "06");
            monthDict.put("Jul", "07");
            monthDict.put("Aug", "08");
            monthDict.put("Sep", "09");
            monthDict.put("Oct", "10");
            monthDict.put("Nov", "11");
            monthDict.put("Dec", "12");

            /* Mapper */
      			// StringTokenizer line = new StringTokenizer(value.toString());

            String line = value.toString().trim();
      			time = line.split("\\[")[1].split("\\]")[0];
            hour = time.split("/")[2].split(":")[1];
      			date = time.split("/")[0];
      			month = monthDict.get(time.split("/")[1]);
      			year = time.split("/")[2].split(":")[0];
      			word.set(year + "-" + month + "-" + date + " T " + hour + ":00:00.000");
            context.write(word, plugOne);
        }
    }

    public static class WordCountReducer
            extends Reducer<Text,IntWritable,Text,IntWritable> {

        private IntWritable result = new IntWritable();

        @Override
        public void reduce(Text key, Iterable<IntWritable> values,
                           Context context
        ) throws IOException, InterruptedException {
            int reduceSum = 0;
            for (IntWritable val : values) {
                reduceSum += val.get();
            }
            result.set(reduceSum);
            context.write(key, result);
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration config = new Configuration();
        Job job = Job.getInstance(config, "hadoop word count example");
        job.setJarByClass(HadoopWordCountSample.class);
        job.setReducerClass(WordCountReducer.class);
        job.setMapperClass(WordCountMapper.class);
        job.setCombinerClass(WordCountReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
