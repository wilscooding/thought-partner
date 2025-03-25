import React, { useState } from "react";
import {
	View,
	Text,
	TextInput,
	Button,
	ScrollView,
	StyleSheet,
	KeyboardAvoidingView,
	Platform,
} from "react-native";
import { useLocalSearchParams } from "expo-router";
import * as Speech from "expo-speech";

const API_URL = "http://127.0.0.1:8000/api/generate_prompt"; // Update to production URL later

const ChatScreen = () => {
	const { industry, capability_area, gender, personality_type } =
		useLocalSearchParams();

	const [userInput, setUserInput] = useState("");
	const [aiResponse, setAiResponse] = useState("");
	const [isFirstMessage, setIsFirstMessage] = useState(true);
	const [conversation, setConversation] = useState<
		{ sender: "user" | "ai"; text: string }[]
	>([]);

	const sendMessage = async () => {
		if (!userInput) return;

		// Add user message to conversation
		setConversation((prev) => [...prev, { sender: "user", text: userInput }]);

		const payload = {
			industry,
			capability_area,
			gender,
			personality_type,
			user_input_text: userInput,
			is_first_message: isFirstMessage,
		};

		try {
			const response = await fetch(API_URL, {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify(payload),
			});

			const data = await response.json();
			const aiMessage = data.ai_response;

			// Add AI message to conversation
			setConversation((prev) => [...prev, { sender: "ai", text: aiMessage }]);
			setAiResponse(aiMessage);
			setUserInput("");

			setIsFirstMessage(false); // Set to false after the first message

			// Speak the response
			Speech.speak(aiMessage, { language: "en-US" });
		} catch (error) {
			console.error("Error communicating with backend:", error);
		}
	};

	return (
		<KeyboardAvoidingView
			style={styles.container}
			behavior={Platform.OS === "ios" ? "padding" : undefined}
		>
			<ScrollView contentContainerStyle={styles.chatContainer}>
				{conversation.map((msg, index) => (
					<View
						key={index}
						style={[
							styles.messageBubble,
							msg.sender === "user" ? styles.userBubble : styles.aiBubble,
						]}
					>
						<Text style={styles.messageText}>{msg.text}</Text>
					</View>
				))}
			</ScrollView>

			<View style={styles.inputContainer}>
				<TextInput
					placeholder="Type your thoughts..."
					value={userInput}
					onChangeText={setUserInput}
					style={styles.input}
				/>
				<Button title="Send" onPress={sendMessage} />
			</View>
		</KeyboardAvoidingView>
	);
};

export default ChatScreen;

const styles = StyleSheet.create({
	container: {
		flex: 1,
	},
	chatContainer: {
		padding: 20,
	},
	messageBubble: {
		padding: 10,
		marginBottom: 10,
		borderRadius: 10,
		maxWidth: "80%",
	},
	userBubble: {
		backgroundColor: "#d0f0ff",
		alignSelf: "flex-end",
	},
	aiBubble: {
		backgroundColor: "#f0f0f0",
		alignSelf: "flex-start",
	},
	messageText: {
		fontSize: 16,
	},
	inputContainer: {
		flexDirection: "row",
		padding: 10,
		borderTopWidth: 1,
		borderColor: "#ccc",
		alignItems: "center",
	},
	input: {
		flex: 1,
		marginRight: 10,
		padding: 10,
		borderWidth: 1,
		borderColor: "#ccc",
		borderRadius: 5,
	},
});
