import pandas as pd

df = pd.read_csv('/content/mock_engagement_data1.csv')
average_metrics = df.groupby("post_type")[['likes', 'shares', 'comments']].mean().reset_index()

print("Average Engagement Metrics:")
print(average_metrics)

output_file_path = "average_engagement_metrics.csv" 
average_metrics.to_csv(output_file_path, index=False)

print(f"Average metrics saved to {output_file_path}")
