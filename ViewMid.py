import mido

# ✅ Fix the path using a raw string
midi_path = r"C:\Users\chris\Desktop\PianoGame\EZ_Piano_03_-_Hot_Cross_Buns.mid"

# Load the MIDI file
mid = mido.MidiFile(midi_path)

# Print General MIDI Info
print("=" * 50)
print(f"🎼 MIDI File Info: Format {mid.type}, Tracks: {len(mid.tracks)}, Ticks per Beat: {mid.ticks_per_beat}")
print("=" * 50)

# Loop through all tracks
for i, track in enumerate(mid.tracks):
    print(f"\n🎵 === Track {i}: {track.name} === 🎵")

    # Separate different message types for clarity
    tempo_events = []
    note_events = []
    control_events = []
    meta_events = []

    for msg in track:
        if msg.type == "set_tempo":
            tempo_events.append(msg)
        elif msg.type in ["note_on", "note_off"]:
            note_events.append(msg)
        elif msg.type == "control_change":
            control_events.append(msg)
        else:
            meta_events.append(msg)

    # Print tempo changes (if any)
    if tempo_events:
        print("\n⏱ Tempo Events:")
        for event in tempo_events:
            bpm = mido.tempo2bpm(event.tempo)
            print(f"   - Set Tempo: {bpm} BPM (Microseconds per beat: {event.tempo})")

    # Print note events
    if note_events:
        print("\n🎹 Note Events:")
        for event in note_events:
            event_type = "ON" if event.type == "note_on" and event.velocity > 0 else "OFF"
            print(f"   - {event_type} | Note: {event.note} | Velocity: {event.velocity} | Time: {event.time}")

    # Print control changes (e.g., sustain pedal)
    if control_events:
        print("\n🎚 Control Events:")
        for event in control_events:
            print(f"   - Control: {event.control} | Value: {event.value} | Time: {event.time}")

    # Print meta events (track names, lyrics, etc.)
    if meta_events:
        print("\n📜 Meta Events:")
        for event in meta_events:
            print(f"   - {event}")

print("\n🎵 MIDI File Printout Complete! 🎵")
