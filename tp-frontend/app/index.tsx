import { View, Text, Button, StyleSheet } from "react-native";
import { router } from "expo-router";

export default function HomeScreen() {
	return (
		<View style={styles.container}>
			<Text style={styles.title}>Welcome to Thought Partner</Text>
			<Text style={styles.subtitle}>
				Tap below to customize your partner and start chatting.
			</Text>
			<Button title="Get Started" onPress={() => router.push("/user-setup")} />
		</View>
	);
}

const styles = StyleSheet.create({
	container: {
		flex: 1,
		justifyContent: "center",
		padding: 24,
		gap: 20,
	},
	title: {
		fontSize: 26,
		fontWeight: "bold",
		textAlign: "center",
	},
	subtitle: {
		fontSize: 16,
		textAlign: "center",
	},
});
