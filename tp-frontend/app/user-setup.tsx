import React, { useEffect, useState } from "react";
import {
	View,
	Text,
	Button,
	ActivityIndicator,
	ScrollView,
	StyleSheet,
} from "react-native";
import { Picker } from "@react-native-picker/picker";
import { router } from "expo-router";

type OptionsResponse = {
	industries: string[];
	capability_areas: string[];
	genders: string[];
	personality_types: string[];
};

type UserSelections = {
	industry: string;
	capability_area: string;
	gender: string;
	personality_type: string;
};

const API_URL = "http://127.0.0.1:8000/api"; // Update for production use

const keyMap: { [key: string]: keyof UserSelections } = {
	industries: "industry",
	capability_areas: "capability_area",
	genders: "gender",
	personality_types: "personality_type",
};

const UserSetup = () => {
	const [options, setOptions] = useState<OptionsResponse | null>(null);
	const [selections, setSelections] = useState<UserSelections>({
		industry: "",
		capability_area: "",
		gender: "",
		personality_type: "",
	});

	useEffect(() => {
		fetch(`${API_URL}/options`)
			.then((res) => res.json())
			.then((data) => setOptions(data))
			.catch((err) => console.error("Error fetching options:", err));
	}, []);

	const handleChange = (key: keyof UserSelections, value: string) => {
		setSelections((prev) => ({ ...prev, [key]: value }));
	};

	const handleContinue = () => {
		console.log("User selections:", selections);

		const allSelected = Object.values(selections).every(Boolean);
		if (!allSelected) {
			alert("Please complete all selections.");
			return;
		}

		router.push({
			pathname: "/chat",
			params: selections,
		});
	};

	if (!options) {
		return <ActivityIndicator size="large" style={{ flex: 1 }} />;
	}

	return (
		<ScrollView contentContainerStyle={styles.container}>
			<Text style={styles.title}>Customize Your Thought Partner</Text>

			{Object.entries(options).map(([key, values]) => {
				const mappedKey = keyMap[key];
				if (!mappedKey) return null;

				return (
					<View key={key} style={styles.pickerGroup}>
						<Text style={styles.label}>{mappedKey.replace(/_/g, " ")}</Text>
						<Picker
							selectedValue={selections[mappedKey]}
							onValueChange={(value) => handleChange(mappedKey, value)}
						>
							<Picker.Item label={`Select ${mappedKey}`} value="" />
							{values.map((val) => (
								<Picker.Item key={val} label={val} value={val} />
							))}
						</Picker>
					</View>
				);
			})}

			<Button title="Continue to Chat" onPress={handleContinue} />
		</ScrollView>
	);
};

export default UserSetup;

const styles = StyleSheet.create({
	container: {
		padding: 20,
		flexGrow: 1,
		justifyContent: "center",
	},
	title: {
		fontSize: 22,
		fontWeight: "600",
		textAlign: "center",
		marginBottom: 30,
	},
	pickerGroup: {
		marginBottom: 20,
	},
	label: {
		fontWeight: "500",
		marginBottom: 5,
	},
});
