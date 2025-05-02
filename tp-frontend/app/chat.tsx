// import React, { useEffect, useState } from "react";
// import {
// 	View,
// 	Text,
// 	TextInput,
// 	Button,
// 	ScrollView,
// 	StyleSheet,
// 	KeyboardAvoidingView,
// 	Platform,
// } from "react-native";
// import { useLocalSearchParams } from "expo-router";
// import * as Speech from "expo-speech";
// import Voice from "@react-native-voice/voice";

// const getAPIUrl = () => {
// 	if (Platform.OS === "android")
// 		return "http://10.0.2.2:8000/api/generate_prompt";
// 	return "http://127.0.0.1:8000/api/generate_prompt";
// };

// const API_URL = getAPIUrl();
// const isWeb = Platform.OS === "web";

// const ChatScreen = () => {
// 	const { industry, capability_area, gender, personality_type } =
// 		useLocalSearchParams();

// 	const [userInput, setUserInput] = useState("");
// 	const [aiResponse, setAiResponse] = useState("");
// 	const [isFirstMessage, setIsFirstMessage] = useState(true);
// 	const [isListening, setIsListening] = useState(false);
// 	const [conversation, setConversation] = useState<
// 		{ sender: "user" | "ai"; text: string }[]
// 	>([]);

// 	useEffect(() => {
// 		if (Platform.OS !== "web") {
// 			Voice.onSpeechResults = (event) => {
// 				if (event.value && event.value.length > 0) {
// 					setUserInput(event.value[0]);
// 				}
// 				setIsListening(false);
// 			};

// 			Voice.onSpeechError = (e) => {
// 				console.error("Voice error:", e);
// 				setIsListening(false);
// 			};

// 			return () => {
// 				Voice.destroy().then(Voice.removeAllListeners);
// 			};
// 		}
// 	}, []);

// 	const sendMessage = async () => {
// 		if (!userInput) {
// 			console.log("[sendMessage] No user input. Skipping send.");
// 			return;
// 		}
// 		console.log("[sendMessage] User input:", userInput);

// 		setConversation((prev) => [...prev, { sender: "user", text: userInput }]);

// 		const payload = {
// 			industry,
// 			capability_area,
// 			gender,
// 			personality_type,
// 			user_input_text: userInput,
// 			is_first_message: isFirstMessage,
// 		};

// 		console.log("[sendMessage] Sending payload to API:", payload);
// 		console.log("[sendMessage] API_URL is:", API_URL);

// 		try {
// 			const response = await fetch(API_URL, {
// 				method: "POST",
// 				headers: { "Content-Type": "application/json" },
// 				body: JSON.stringify(payload),
// 			});

// 			console.log("[sendMessage] Fetch completed. Status:", response.status);

// 			const data = await response.json();
// 			console.log("[sendMessage] Data received from API:", data);
// 			const aiMessage = data.ai_response;

// 			setConversation((prev) => [...prev, { sender: "ai", text: aiMessage }]);
// 			setAiResponse(aiMessage);
// 			setUserInput("");
// 			setIsFirstMessage(false);

// 			Speech.speak(aiMessage, { language: "en-US" });
// 		} catch (error) {
// 			console.error("Error communicating with backend:", error);
// 		}
// 	};

// 	const startWebVoiceInput = () => {
// 		const SpeechRecognition =
// 			window.SpeechRecognition || window.webkitSpeechRecognition;
// 		if (!SpeechRecognition) {
// 			alert("Speech recognition not supported in this browser.");
// 			return;
// 		}

// 		const recognition = new SpeechRecognition();
// 		recognition.continuous = false;
// 		recognition.lang = "en-US";

// 		setIsListening(true);
// 		recognition.start();

// 		recognition.onresult = (event: any) => {
// 			const transcript = event.results[0][0].transcript;
// 			setUserInput(transcript);
// 			setIsListening(false);
// 		};

// 		recognition.onerror = (event: any) => {
// 			console.error("Web Speech API error:", event);
// 			setIsListening(false);
// 		};

// 		recognition.onend = () => {
// 			setIsListening(false);
// 		};
// 	};

// 	const startMobileVoiceInput = async () => {
// 		try {
// 			setIsListening(true);
// 			await Voice.start("en-US");
// 		} catch (e) {
// 			console.error("Voice start error:", e);
// 			setIsListening(false);
// 		}
// 	};

// 	const startVoiceInput = () => {
// 		if (isWeb) {
// 			startWebVoiceInput();
// 		} else {
// 			startMobileVoiceInput();
// 		}
// 	};

// 	return (
// 		<KeyboardAvoidingView
// 			style={styles.container}
// 			behavior={Platform.OS === "ios" ? "padding" : undefined}
// 		>
// 			<ScrollView contentContainerStyle={styles.chatContainer}>
// 				{conversation.map((msg, index) => (
// 					<View
// 						key={index}
// 						style={[
// 							styles.messageBubble,
// 							msg.sender === "user" ? styles.userBubble : styles.aiBubble,
// 						]}
// 					>
// 						<Text style={styles.messageText}>{msg.text}</Text>
// 					</View>
// 				))}
// 			</ScrollView>

// 			<View style={styles.inputContainer}>
// 				<TextInput
// 					placeholder={
// 						isListening ? "Listening..." : "Type or speak your thoughts..."
// 					}
// 					value={userInput}
// 					onChangeText={setUserInput}
// 					style={styles.input}
// 				/>
// 				<Button title="🎤" onPress={startVoiceInput} />
// 				<Button title="Send" onPress={sendMessage} />
// 			</View>
// 		</KeyboardAvoidingView>
// 	);
// };

// export default ChatScreen;

// const styles = StyleSheet.create({
// 	container: {
// 		flex: 1,
// 	},
// 	chatContainer: {
// 		padding: 20,
// 	},
// 	messageBubble: {
// 		padding: 10,
// 		marginBottom: 10,
// 		borderRadius: 10,
// 		maxWidth: "80%",
// 	},
// 	userBubble: {
// 		backgroundColor: "#d0f0ff",
// 		alignSelf: "flex-end",
// 	},
// 	aiBubble: {
// 		backgroundColor: "#f0f0f0",
// 		alignSelf: "flex-start",
// 	},
// 	messageText: {
// 		fontSize: 16,
// 	},
// 	inputContainer: {
// 		flexDirection: "row",
// 		padding: 10,
// 		borderTopWidth: 1,
// 		borderColor: "#ccc",
// 		alignItems: "center",
// 	},
// 	input: {
// 		flex: 1,
// 		marginRight: 10,
// 		padding: 10,
// 		borderWidth: 1,
// 		borderColor: "#ccc",
// 		borderRadius: 5,
// 	},
// });

import React, { useEffect, useState } from "react";
import {
	View,
	Text,
	TextInput,
	Button,
	ScrollView,
	StyleSheet,
	KeyboardAvoidingView,
	Platform,
	PermissionsAndroid,
	Alert,
} from "react-native";
import { useLocalSearchParams } from "expo-router";
import * as Speech from "expo-speech";
import Voice from "@react-native-voice/voice";

const getAPIUrl = () => {
	if (Platform.OS === "android") {
		// return "http://192.168.1.219:8000/api/generate_prompt";
		return "http://10.0.2.2:8000/api/generate_prompt";
	}
	// return "http://192.168.1.219:8000/api/generate_prompt";
	return "http://127.0.0.1:8000/api/generate_prompt";
};

const API_URL = getAPIUrl();
const isWeb = Platform.OS === "web";

declare global {
	interface Window {
		SpeechRecognition: any;
		webkitSpeechRecognition: any;
	}
}

const ChatScreen = () => {
	const { industry, capability_area, gender, personality_type } =
		useLocalSearchParams();

	const [userInput, setUserInput] = useState("");
	const [isFirstMessage, setIsFirstMessage] = useState(true);
	const [isListening, setIsListening] = useState(false);
	const [conversation, setConversation] = useState<
		{ sender: "user" | "ai"; text: string }[]
	>([]);

	useEffect(() => {
		if (!isWeb) {
			Voice.onSpeechResults = (event) => {
				if (event.value?.length) {
					setUserInput(event.value[0]);
				}
				setIsListening(false);
			};

			Voice.onSpeechError = (e) => {
				console.error("Voice error:", e);
				setIsListening(false);
			};

			return () => {
				Voice.destroy().then(Voice.removeAllListeners);
			};
		}
	}, []);

	const sendMessage = async () => {
		if (!userInput) return;

		const newMessage = { sender: "user" as const, text: userInput };
		setConversation((prev) => [...prev, newMessage]);

		const payload = {
			industry,
			capability_area,
			gender,
			personality_type,
			user_input_text: userInput,
			is_first_message: isFirstMessage,
		};

		try {
			console.log("Sending to API:", API_URL, payload);

			const response = await fetch(API_URL, {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify(payload),
			});

			const data = await response.json();
			const aiMessage = data.ai_response;

			setConversation((prev) => [...prev, { sender: "ai", text: aiMessage }]);
			setUserInput("");
			setIsFirstMessage(false);

			Speech.speak(aiMessage, { language: "en-US" });
		} catch (error) {
			console.error("Error communicating with backend:", error);
		}
	};

	const startWebVoiceInput = () => {
		const SpeechRecognition =
			window.SpeechRecognition || window.webkitSpeechRecognition;
		if (!SpeechRecognition) {
			alert("Speech recognition not supported in this browser.");
			return;
		}

		const recognition = new SpeechRecognition();
		recognition.lang = "en-US";
		setIsListening(true);
		recognition.start();

		recognition.onresult = (event: any) => {
			const transcript = event.results[0][0].transcript;
			setUserInput(transcript);
			setIsListening(false);
		};

		recognition.onerror = (event: any) => {
			console.error("Speech error:", event);
			setIsListening(false);
		};

		recognition.onend = () => {
			setIsListening(false);
		};
	};

	const startMobileVoiceInput = async () => {
		try {
			if (Platform.OS === "android") {
				const granted = await PermissionsAndroid.request(
					PermissionsAndroid.PERMISSIONS.RECORD_AUDIO,
					{
						title: "Microphone Permission",
						message: "This app needs microphone access for voice input.",
						buttonNeutral: "Ask Me Later",
						buttonNegative: "Cancel",
						buttonPositive: "OK",
					}
				);

				if (granted !== PermissionsAndroid.RESULTS.GRANTED) {
					Alert.alert(
						"Permission Denied",
						"Microphone permission is required to use voice input."
					);
					setIsListening(false);
					return;
				}
			}

			setIsListening(true);
			await Voice.start("en-US");
		} catch (e) {
			console.error("Voice start error:", e);
			setIsListening(false);
		}
	};

	const startVoiceInput = () => {
		if (isWeb) {
			startWebVoiceInput();
		} else {
			startMobileVoiceInput();
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
					placeholder={
						isListening ? "Listening..." : "Type or speak your thoughts..."
					}
					value={userInput}
					onChangeText={setUserInput}
					style={styles.input}
				/>
				<Button title="🎤" onPress={startVoiceInput} />
				<Button title="Send" onPress={sendMessage} />
			</View>
		</KeyboardAvoidingView>
	);
};

export default ChatScreen;

const styles = StyleSheet.create({
	container: { flex: 1 },
	chatContainer: { padding: 20 },
	messageBubble: {
		padding: 10,
		marginBottom: 10,
		borderRadius: 10,
		maxWidth: "80%",
	},
	userBubble: { backgroundColor: "#d0f0ff", alignSelf: "flex-end" },
	aiBubble: { backgroundColor: "#f0f0f0", alignSelf: "flex-start" },
	messageText: { fontSize: 16 },
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
