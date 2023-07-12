"""Module for testing dock widgets for the `MainWindow`."""

import pytest

from sleap import Labels, Video
from sleap.gui.app import MainWindow
from sleap.gui.widgets.docks import (
    InstancesDock,
    SuggestionsDock,
    VideosDock,
    SkeletonDock,
)


def test_videos_dock(qtbot, centered_pair_predictions: Labels,
    small_robot_mp4_vid: Video,
    centered_pair_vid: Video,
    small_robot_3_frame_vid: Video,):
    """Test the `DockWidget` class."""
    
    # Add some extra videos to the labels
    labels = centered_pair_predictions
    labels.add_video(small_robot_mp4_vid)
    labels.add_video(centered_pair_vid)
    labels.add_video(small_robot_3_frame_vid)
    assert len(labels.videos) == 4

    # Create the dock
    main_window = MainWindow()
    main_window.labels = labels
    video_state = labels.videos[-1]
    main_window.state["video"] = video_state
    dock = VideosDock(main_window)

    # Test that the dock was created correctly
    assert dock.name == "Videos"
    assert dock.main_window is main_window
    assert dock.wgt_layout is dock.widget().layout()

    # Test that videos can be removed

    # No videos selected, should remove the state video
    dock.main_window._buttons["remove video"].click()
    assert len(labels.videos) == 3
    assert video_state not in labels.videos
    assert main_window.state["video"] == labels.videos[-1]

    # TODO(LM): Select the first video, should remove that one and update state
    
    # TODO(LM): Select the last two videos, should remove those two and update state



def test_skeleton_dock(qtbot):
    """Test the `DockWidget` class."""
    main_window = MainWindow()
    dock = SkeletonDock(main_window)

    assert dock.name == "Skeleton"
    assert dock.main_window is main_window
    assert dock.wgt_layout is dock.widget().layout()


def test_suggestions_dock(qtbot):
    """Test the `DockWidget` class."""
    main_window = MainWindow()
    dock = SuggestionsDock(main_window)

    assert dock.name == "Labeling Suggestions"
    assert dock.main_window is main_window
    assert dock.wgt_layout is dock.widget().layout()


def test_instances_dock(qtbot):
    """Test the `DockWidget` class."""
    main_window = MainWindow()
    dock = InstancesDock(main_window)

    assert dock.name == "Instances"
    assert dock.main_window is main_window
    assert dock.wgt_layout is dock.widget().layout()


# TODO(LM): Remove test code before merging
if __name__ == "__main__":
    pytest.main([f"{__file__}::test_videos_dock"])
